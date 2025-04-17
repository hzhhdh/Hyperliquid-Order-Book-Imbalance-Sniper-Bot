use ethers::prelude::*;
use std::sync::Arc;

/// Uniswap V3 pool ABI (concentrated liquidity)
abigen!(
    UniswapV3Pool,
    r#"[
        function observe(uint32[] secondsAgos) external view returns (int56[] tickCumulatives, uint160[] secondsPerLiquidityCumulativeX128s)
        function slot0() external view returns (uint160 sqrtPriceX96, int24 tick, uint16 observationIndex, uint16 observationCardinality, uint16 observationCardinalityNext, uint8 feeProtocol, bool unlocked)
    ]"#,
);

/// Query current price and liquidity from a Uniswap V3 pool on Polygon
pub async fn polygon_query_v3_liquidity(
    client: Arc<Provider<Http>>,
    pool_address: Address,
) -> Result<(U256, i128), ContractError<Provider<Http>>> {
    let pool = UniswapV3Pool::new(pool_address, client.clone());
    let (sqrt_price_x96, tick, _, _, _, _, _) = pool.slot0().call().await?;
    // Convert sqrtPriceX96 to price: price = (sqrt_price_x96)^2 / Q96^2
    let price = U256::from(sqrt_price_x96) * U256::from(sqrt_price_x96) >> (96 * 2);
    Ok((price, tick.into()))
}

/// Provide liquidity into a Uniswap V3 pool (requires NFT minting — simplified)
/// **Note:** full V3 liquidity provision requires complex calldata; here we stub the logic.
pub async fn polygon_provide_liquidity(
    client: Arc<SignerMiddleware<Provider<Http>, WalletSigner>>,
    position_manager: Address,
    token0: Address,
    token1: Address,
    fee: u32,
    tick_lower: i32,
    tick_upper: i32,
    amount0: U256,
    amount1: U256,
) -> Result<TxHash, Box<dyn std::error::Error>> {
    // Use UniswapV3PositionManager to mint a new liquidity position
    let pm = UniswapV3PositionManager::new(position_manager, client.clone());
    let deadline = U256::from((chrono::Utc::now().timestamp() + 600) as u64);
    let params = pm.mint(
        MintParams {
            token0,
            token1,
            fee,
            tick_lower,
            tick_upper,
            amount0_desired: amount0,
            amount1_desired: amount1,
            amount0_min: U256::zero(),
            amount1_min: U256::zero(),
            recipient: client.address(),
            deadline,
        }
    );
    let tx = params.send().await?;
    Ok(tx.tx_hash())
}
