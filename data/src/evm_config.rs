use ethers::prelude::*;
use std::convert::TryFrom;
use std::sync::Arc;
use std::time::Duration;

/// Holds RPC URLs and chain IDs for EVM networks
pub struct EvmConfig {
    pub ethereum_rpc: String,
    pub polygon_rpc: String,
    pub bsc_rpc: String,
    pub base_network_rpc: String,
    pub arbitrum_rpc: String,
    pub chain_id: u64,
}

impl EvmConfig {
    pub fn load_from_env() -> Self {
        dotenv::dotenv().ok();
        Self {
            ethereum_rpc: std::env::var("ETHEREUM_RPC_URL").expect("Missing ETHEREUM_RPC_URL"),
            polygon_rpc: std::env::var("POLYGON_RPC_URL").expect("Missing POLYGON_RPC_URL"),
            bsc_rpc: std::env::var("BSC_RPC_URL").expect("Missing BSC_RPC_URL"),
            base_network_rpc: std::env::var("BASE_NETWORK_RPC_URL").expect("Missing BASE_NETWORK_RPC_URL"),
            arbitrum_rpc: std::env::var("ARBITRUM_RPC_URL").expect("Missing ARBITRUM_RPC_URL"),
            chain_id: std::env::var("CHAIN_ID").unwrap_or_else(|_| "1".into()).parse().unwrap(),
        }
    }

    pub async fn provider(&self, network: &str) -> Provider<Http> {
        let url = match network {
            "ethereum" => &self.ethereum_rpc,
            "polygon"  => &self.polygon_rpc,
            "bsc"      => &self.bsc_rpc,
            "base"     => &self.base_network_rpc,
            "arbitrum" => &self.arbitrum_rpc,
            _ => panic!("Unknown network"),
        };
        Provider::<Http>::try_from(url.as_str())
            .expect("invalid RPC URL")
            .interval(Duration::from_millis(200u64))
    }
}
