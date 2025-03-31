use reqwest::Client;
use serde_json::json;

pub async fn send_mev_protected_tx(tx_data: &str) -> Result<String, reqwest::Error> {
    let client = Client::new();
    let response = client
        .post("https://relay.flashbots.net")
        .json(&json!({"tx": tx_data}))
        .send()
        .await?;
    
    response.text().await
}
