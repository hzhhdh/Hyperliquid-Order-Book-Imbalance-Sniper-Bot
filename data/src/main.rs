mod evm_config;
mod uniswap_integration;
mod one_inch_integration;
mod token_liquidity;
mod trading_manager;

use evm_config::EvmConfig;
use trading_manager::TradingManager;
use ethers::middleware::SignerMiddleware;
use ethers::providers::Provider;
use ethers::signers::{LocalWallet, Signer};
use ethers::types::Address;
use std::sync::Arc;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Load configuration
    let config = EvmConfig::load_from_env();

    // Setup wallet signer (Ethereum by default)
    let provider = config.provider("ethereum").await;
    let wallet: LocalWallet = std::env::var("PRIVATE_KEY")?.parse()?;
    let wallet = wallet.with_chain_id(config.chain_id);
    let client = SignerMiddleware::new(provider.clone(), wallet);
    let client = Arc::new(client);

    // Initialize trading manager
    let manager = TradingManager::new(config);

    // Example: compare quotes and trade 10 tokens on Ethereum
    let token_in: Address = "0xTokenInAddress".parse()?;
    let token_out: Address = "0xTokenOutAddress".parse()?;
    let router: Address = "0xUniswapRouter".parse()?;
    let amount_in = U256::from_dec_str("10000000000000000000")?; // 10 tokens

    manager
        .execute_best_trade("ethereum", client.clone(), router, token_in, token_out, amount_in)
        .await?;

    // Monitor liquidity on Polygon
    let pair_address: Address = "0xPairAddress".parse()?;
    manager.monitor_token_liquidity("polygon", pair_address).await?;

    Ok(())
}
