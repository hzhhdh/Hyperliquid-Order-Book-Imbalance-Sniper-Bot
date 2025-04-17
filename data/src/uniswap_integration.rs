use ethers::prelude::*;
use std::sync::Arc;

/// Type-safe Uniswap V2 Router binding
abigen!(
    UniswapV2Router,
    r#"[
        function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) returns (uint[] memory amounts)
        function getAmountsOut(uint amountIn, address[] calldata path) view returns (uint[] memory amounts)
    ]"#,
);

/// Swap tokens via Uniswap on any EVM chain
pub async fn uniswap_trade(
    client: Arc<SignerMiddleware<Provider<Http>, WalletSigner>>,
    router: Address,
    path: Vec<Address>,
    amount_in: U256,
    min_amount_out: U256,
) -> Result<TxHash, ContractError<SignerMiddleware<Provider<Http>, WalletSigner>>> {
    let router = UniswapV2Router::new(router, client.clone());
    let deadline = U256::from((chrono::Utc::now().timestamp() + 600) as u64);

    // Approve input token
    let erc20 = IERC20::new(path[0], client.clone());
    erc20.approve(router.address(), amount_in).send().await?.await?;

    let tx = router
        .swap_exact_tokens_for_tokens(amount_in, min_amount_out, path, client.address(), deadline)
        .send()
        .await?;
    Ok(tx.tx_hash())
}

/// Query expected output via Uniswap
pub async fn uniswap_get_quote(
    client: Arc<Provider<Http>>,
    router: Address,
    path: Vec<Address>,
    amount_in: U256,
) -> Result<U256, ContractError<Provider<Http>>> {
    let router = UniswapV2Router::new(router, client.clone());
    let amounts = router.get_amounts_out(amount_in, path).call().await?;
    Ok(amounts[1])
}
