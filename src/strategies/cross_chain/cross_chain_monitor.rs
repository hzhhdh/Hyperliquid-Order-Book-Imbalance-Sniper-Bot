use reqwest::Client;
use serde::Deserialize;
use log::{info, error};

#[derive(Deserialize)]
struct BridgeData {
    fees: f64,
    latency: u64,
}

struct CrossChainMonitor {
    client: Client,
    api_url: String,
}

impl CrossChainMonitor {
    pub fn new(api_url: &str) -> Self {
        Self {
            client: Client::new(),
            api_url: api_url.to_string(),
        }
    }

    pub async fn fetch_bridge_data(&self, src_chain: u32, dst_chain: u32) -> Result<BridgeData, Box<dyn std::error::Error>> {
        let url = format!("{}?srcChain={}&dstChain={}", self.api_url, src_chain, dst_chain);
        let resp = self.client.get(&url).send().await?;
        let data = resp.json::<BridgeData>().await?;
        Ok(data)
    }

    pub async fn monitor(&self, src_chain: u32, dst_chain: u32, fee_threshold: f64) {
        match self.fetch_bridge_data(src_chain, dst_chain).await {
            Ok(data) if data.fees > fee_threshold => {
                info!("High bridge fees: {} for {}->{}", data.fees, src_chain, dst_chain);
            }
            Ok(data) => info!("Bridge fees acceptable: {}", data.fees),
            Err(e) => error!("Error fetching bridge data: {}", e),
        }
    }
}

#[tokio::main]
async fn main() {
    env_logger::init();
    let monitor = CrossChainMonitor::new("https://api.layerzero.network/v1/bridge");
    monitor.monitor(1, 56, 0.01).await; // Ethereum to BSC
}
