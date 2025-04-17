use crate::evm_config::EvmConfig;
use crate::uniswap_integration::{uniswap_trade, uniswap_get_quote};
use crate::one_inch_integration::{one_inch_get_quote};
use crate::token_liquidity::{query_token_liquidity};
use ethers::middleware::SignerMiddleware;
use ethers::providers::Provider;
use ethers::signers::WalletSigner;
use ethers::types::U256;
use std::sync::Arc;
use reqwest::Client;

/// High‑level manager orchestrating multi‑DEX trading
pub struct TradingManager {
    pub config: EvmConfig,
    pub http: Client,
}

impl TradingManager {
    pub fn new(config: EvmConfig) -> Self {
        Self { config, http: Client::new() }
    }

    /// Compare quotes on Uniswap and 1inch, pick best route, and execute a trade
    pub async fn execute_best_trade(
        &self,
        network: &str,
        wallet: Arc<SignerMiddleware<Provider<Http>, WalletSigner>>,
        router: Address,
        token_in: Address,
        token_out: Address,
        amount_in: U256,
    ) -> Result<(), Box<dyn std::error::Error>> {
        // Fetch providers
        let provider = self.config.provider(network).await;
        let client = Arc::new(wallet.clone().with_provider(provider.clone()));

        // Get Uniswap quote
        let uni_quote = uniswap_get_quote(provider.clone(), router, vec![token_in, token_out], amount_in).await?;
        // Get 1inch quote
        let base_chain_id = match network {
            "ethereum" => "1",
            "polygon"  => "137",
            "bsc"      => "56",
            "arbitrum" => "42161",
            _ => panic!("unsupported"),
        };
        let inch_quote = one_inch_get_quote(&self.http, base_chain_id, &format!("{:?}", token_in), &format!("{:?}", token_out), amount_in).await?;

        // Choose the best
        if uni_quote >= inch_quote {
            println!("Using Uniswap route: {}", uni_quote);
            let tx = uniswap_trade(client.clone(), router, vec![token_in, token_out], amount_in, uni_quote).await?;
            println!("Uniswap TX: {:?}", tx);
        } else {
            println!("Using 1inch route: {}", inch_quote);
            // Build tx_data via 1inch API (omitted) then:
            // let tx = one_inch_swap(client.clone(), tx_data).await?;
            // println!("1inch TX: {:?}", tx);
        }

        Ok(())
    }

    /// Monitor token liquidity across chains
    pub async fn monitor_token_liquidity(
        &self,
        network: &str,
        pair_address: Address,
    ) -> Result<(), Box<dyn std::error::Error>> {
        let provider = self.config.provider(network).await;
        let (r0, r1) = query_token_liquidity(Arc::new(provider), pair_address).await?;
        println!("{} liquidity: {} / {}", network, r0, r1);
        Ok(())
    }
}
