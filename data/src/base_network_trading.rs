use ethers::prelude::*;
use std::sync::Arc;

/// Simple router interaction for “Base” network Uniswap V2 forks
abigen!(
    BaseSwapRouter,
    r#"[
        function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) returns (uint[] memory)
    ]"#,
);

/// Execute a Base‑network token swap via a UniswapV2‑style router
pub async fn base_network_swap(
    client: Arc<SignerMiddleware<Provider<Http>, WalletSigner>>,
    router_address: Address,
    path: Vec<Address>,
    amount_in: U256,
    min_amount_out: U256,
) -> Result<TxHash, ContractError<SignerMiddleware<Provider<Http>, WalletSigner>>> {
    let router = BaseSwapRouter::new(router_address, client.clone());
    // Approve token_in
    let erc20 = IERC20::new(path[0], client.clone());
    erc20.approve(router_address, amount_in).send().await?.await?;
    let deadline = U256::from((chrono::Utc::now().timestamp() + 300) as u64);
    let tx = router
        .swap_exact_tokens_for_tokens(amount_in, min_amount_out, path, client.address(), deadline)
        .gas_price(U256::from(5_000_000_000u64)) // 5 Gwei on Base
        .send()
        .await?;
    Ok(tx.tx_hash())
}
