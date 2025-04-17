use ethers::prelude::*;
use std::sync::Arc;

/// ABI for Uniswap V2 pair (liquidity pool)
abigen!(
    UniswapV2Pair,
    r#"[
        function getReserves() view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast)
        function mint(address to) returns (uint liquidity)
        function burn(address to) returns (uint amount0, uint amount1)
    ]"#,
);

/// Query token liquidity from a pool
pub async fn query_token_liquidity(
    client: Arc<Provider<Http>>,
    pair_address: Address
) -> Result<(U256, U256), ContractError<Provider<Http>>> {
    let pair = UniswapV2Pair::new(pair_address, client.clone());
    let (r0, r1, _) = pair.get_reserves().call().await?;
    Ok((U256::from(r0), U256::from(r1)))
}

/// Add liquidity to pool (requires approvals)
pub async fn add_liquidity(
    client: Arc<SignerMiddleware<Provider<Http>, WalletSigner>>,
    pair_address: Address,
    amount0: U256,
    amount1: U256,
) -> Result<TxHash, ContractError<SignerMiddleware<Provider<Http>, WalletSigner>>> {
    let pair = UniswapV2Pair::new(pair_address, client.clone());
    // Assumes ERC20 approvals done upstream
    let tx = pair.mint(client.address()).send().await?;
    Ok(tx.tx_hash())
}

/// Remove liquidity from pool
pub async fn remove_liquidity(
    client: Arc<SignerMiddleware<Provider<Http>, WalletSigner>>,
    pair_address: Address,
) -> Result<TxHash, ContractError<SignerMiddleware<Provider<Http>, WalletSigner>>> {
    let pair = UniswapV2Pair::new(pair_address, client.clone());
    let tx = pair.burn(client.address()).send().await?;
    Ok(tx.tx_hash())
}
