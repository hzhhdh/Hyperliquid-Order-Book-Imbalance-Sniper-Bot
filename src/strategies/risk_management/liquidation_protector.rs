use ethers::prelude::*;
use log::{info, error};

struct LiquidationProtector {
    provider: Provider<Http>,
    chainlink_feed: Address,
}

impl LiquidationProtector {
    pub fn new(provider_url: &str, chainlink_feed: &str) -> Self {
        let provider = Provider::<Http>::try_from(provider_url).expect("Invalid provider URL");
        let chainlink_feed = chainlink_feed.parse().expect("Invalid address");
        Self { provider, chainlink_feed }
    }

    pub async fn fetch_health_factor(&self, user: &str) -> Result<f64, Box<dyn std::error::Error>> {
        // Placeholder: Fetch Aave health factor
        Ok(1.8)
    }

    pub async fn protect(&self, user: &str, threshold: f64) {
        match self.fetch_health_factor(user).await {
            Ok(health) if health < threshold => {
                // TODO: Repay loan
                info!("Repaid loan for user {}, health factor: {}", user, health);
            }
            Ok(health) => info!("Health factor acceptable: {}", health),
            Err(e) => error!("Error checking health factor: {}", e),
        }
    }
}

#[tokio::main]
async fn main() {
    env_logger::init();
    let protector = LiquidationProtector::new("https://mainnet.infura.io/v3/YOUR_PROJECT_ID", "0x...");
    protector.protect("0x...", 1.5).await;
}
