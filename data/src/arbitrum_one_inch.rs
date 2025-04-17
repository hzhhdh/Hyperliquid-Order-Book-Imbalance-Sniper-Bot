use ethers::prelude::*;
use reqwest::Client;
use serde::Deserialize;
use std::sync::Arc;

/// 1inch quote response on Arbitrum
#[derive(Deserialize)]
pub struct ArbitrumQuote { pub toTokenAmount: String }

/// Get best Arbitrum route via 1inch
pub async fn arbitrum_get_best_quote(
    http: &Client,
    token_in: &str,
    token_out: &str,
    amount: U256,
) -> Result<U256, Box<dyn std::error::Error>> {
    let url = format!(
        "https://api.1inch.io/v5.0/42161/quote?fromTokenAddress={}&toTokenAddress={}&amount={}",
        token_in, token_out, amount
    );
    let resp = http.get(&url).send().await?.json::<ArbitrumQuote>().await?;
    Ok(U256::from_dec_str(&resp.toTokenAmount)?)
}

/// Build and send the 1inch swap transaction on Arbitrum
pub async fn arbitrum_execute_one_inch(
    client: Arc<SignerMiddleware<Provider<Http>, WalletSigner>>,
    tx_data: Bytes,
) -> Result<TxHash, Box<dyn std::error::Error>> {
    let pending = client.send_raw_transaction(tx_data).await?;
    Ok(pending.tx_hash())
}
