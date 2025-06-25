use serde_json::Value;
use reqwest::Client;

/// Scan Meteora pools for new tokens
pub async fn scan_meteora_pools(min_liquidity: f64) -> Result<Vec<String>, Box<dyn std::error::Error>> {
    let client = Client::new();
    let response = client.get("https://api.dexscreener.com/latest/dex/tokens/").send().await?;
    let pools: Value = response.json().await?;

    let mut new_pools = Vec::new();
    if let Some(pairs) = pools["pairs"].as_array() {
        for pool in pairs {
            if pool["dexId"].as_str() == Some("meteora") &&
               pool["liquidity"]["usd"].as_f64().unwrap_or(0.0) > min_liquidity {
                new_pools.push(pool["baseToken"]["address"].as_str().unwrap_or("").to_string());
            }
        }
    }
    Ok(new_pools)
}
