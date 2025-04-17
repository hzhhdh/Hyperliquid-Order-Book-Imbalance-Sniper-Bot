abigen!(
    MasterChef,
    r#"[
        function deposit(uint256 pid, uint256 amount)
        function withdraw(uint256 pid, uint256 amount)
        function claim(uint256 pid)
    ]"#,
);

/// Deposit LP tokens into liquidity mining contract
async fn stake_lp(
    client: Arc<SignerMiddleware<GasEscalator<Provider<Http>>, LocalWallet>>,
    chef_address: Address,
    pid: u64,
    amount_lp: U256,
) -> Result<TxHash, Box<dyn std::error::Error>> {
    let chef = MasterChef::new(chef_address, client.clone());
    // Approve LP token
    let lp_token = IERC20::new(chef.address(), client.clone());
    lp_token.approve(chef_address, amount_lp).send().await?.await?;

    let tx = chef.deposit(U256::from(pid), amount_lp).send().await?;
    Ok(tx.tx_hash())
}

/// Claim rewards from liquidity mining
async fn claim_rewards(
    client: Arc<SignerMiddleware<GasEscalator<Provider<Http>>, LocalWallet>>,
    chef_address: Address,
    pid: u64,
) -> Result<TxHash, Box<dyn std::error::Error>> {
    let chef = MasterChef::new(chef_address, client.clone());
    let tx = chef.claim(U256::from(pid)).send().await?;
    Ok(tx.tx_hash())
}
