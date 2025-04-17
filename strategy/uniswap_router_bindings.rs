// Generate type-safe bindings from the Uniswap V2 Router ABI
abigen!(
    UniswapV2Router,
    r#"[
        function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) payable returns (uint[] memory amounts)
        function swapExactTokensForETH(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) returns (uint[] memory amounts)
    ]"#,
);

/// Buys `token_out` using ETH
async fn buy_token(
    client: Arc<SignerMiddleware<GasEscalator<Provider<Http>>, LocalWallet>>,
    router_address: Address,
    token_out: Address,
    amount_eth: U256,
    min_tokens_out: U256,
) -> Result<TxHash, Box<dyn std::error::Error>> {
    let router = UniswapV2Router::new(router_address, client.clone());
    let path = vec![client.address(), token_out];
    let deadline = U256::from((std::time::SystemTime::now()
        + std::time::Duration::from_secs(300))
        .duration_since(std::time::UNIX_EPOCH)?
        .as_secs());

    let tx = router
        .swap_exact_eth_for_tokens(min_tokens_out, path, client.address(), deadline)
        .value(amount_eth)
        .gas_price(U256::from(20_000_000_000u64))      // 20 Gwei
        .send()
        .await?;
    Ok(tx.tx_hash())
}

/// Sells `token_in` for ETH
async fn sell_token(
    client: Arc<SignerMiddleware<GasEscalator<Provider<Http>>, LocalWallet>>,
    router_address: Address,
    token_in: Address,
    amount_in: U256,
    min_eth_out: U256,
) -> Result<TxHash, Box<dyn std::error::Error>> {
    let router = UniswapV2Router::new(router_address, client.clone());
    let path = vec![token_in, client.address()];
    let deadline = U256::from((std::time::SystemTime::now()
        + std::time::Duration::from_secs(300))
        .duration_since(std::time::UNIX_EPOCH)?
        .as_secs());
    
    // Approve token spending
    let erc20 = IERC20::new(token_in, client.clone());
    erc20.approve(router_address, amount_in).send().await?.await?;

    let tx = router
        .swap_exact_tokens_for_eth(amount_in, min_eth_out, path, client.address(), deadline)
        .gas_price(U256::from(20_000_000_000u64))
        .send()
        .await?;
    Ok(tx.tx_hash())
}
