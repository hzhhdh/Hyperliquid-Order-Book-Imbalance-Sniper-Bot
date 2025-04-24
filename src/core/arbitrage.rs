use web3::types::U256;
use crate::dex::{PancakeSwap, ApeSwap};

pub async fn execute_arbitrage() -> Result<(), String> {
    let pancake_price = PancakeSwap::get_price("BNB/USDT").await?;
    let ape_price = ApeSwap::get_price("BNB/USDT").await?;
    
    if let Some(profit) = calculate_profit(pancake_price, ape_price) {
        if profit > U256::from(1000000000000000) { // 0.1% threshold
            let tx_hash = PancakeSwap::sell("BNB", profit).await?;
            log::info!("Arbitrage executed: {}", tx_hash);
        }
    }
    Ok(())
}
