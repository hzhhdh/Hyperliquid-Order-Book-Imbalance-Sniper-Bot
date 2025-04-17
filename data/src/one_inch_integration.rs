use reqwest::Client;
use serde::Deserialize;
use ethers::types::U256;

/// 1inch quote response
#[derive(Deserialize)]
pub struct OneInchQuote {
    pub toTokenAmount: String,
}

/// Fetch a 1inch swap quote
pub async fn one_inch_get_quote(
    client: &Client,
    network: &str,
    token_in: &str,
    token_out: &str,
    amount: U256,
) -> Result<U256, Box<dyn std::error::Error>> {
    let url = format!(
        "https://api.1inch.io/v5.0/{}/quote?fromTokenAddress={}&toTokenAddress={}&amount={}",
        network, token_in, token_out, amount
    );
    let resp = client.get(&url).send().await?.json::<OneInchQuote>().await?;
    Ok(U256::from_dec_str(&resp.toTokenAmount)?)
}

/// Execute swap via 1inch Router contract
pub async fn one_inch_swap(
    client: Arc<SignerMiddleware<Provider<Http>, WalletSigner>>,
    tx_data: Bytes,
) -> Result<TxHash, Box<dyn std::error::Error>> {
    // 1inch returns `tx` object; we only need to send data
    let tx = client.send_transaction(tx_data.into(), None).await?;
    Ok(tx.tx_hash())
}
