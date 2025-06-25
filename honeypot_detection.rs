use serde_json::Value;
use reqwest::Client;

/// Detect honeypot tokens by holder distribution
pub async fn detect_honeypot(token_address: &str, max_holder_share: f64) -> Result<bool, Box<dyn std::error::Error>> {
    let client = Client::new();
    let response = client.get(&format!("https://public-api.solscan.io/token/holders?tokenAddress={}", token_address))
        .send().await?;
    let holders: Value = response.json().await?;

    let mut total_supply = 0.0;
    let mut top_holder_share = 0.0;

    if let Some(data) = holders["data"].as_array() {
        for holder in data {
            let amount = holder["amount"].as_f64().unwrap_or(0.0);
            total_supply += amount;
            top_holder_share = top_holder_share.max(amount);
        }
    }

    Ok(top_holder_share / total_supply <= max_holder_share)
}
