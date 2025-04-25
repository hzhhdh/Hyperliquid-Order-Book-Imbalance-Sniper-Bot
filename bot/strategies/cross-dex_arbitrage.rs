use reqwest;
use tokio;

#[tokio::main]
async fn execute_arbitrage(token: &str, amount: f64) -> Result<(), reqwest::Error> {
    let uni_price = reqwest::get(format!("https://api.uniswap.org/price/{}", token))
        .await?
        .json::<f64>()
        .await?;

    let dydx_price = reqwest::get(format!("https://api.dydx.org/perps/{}", token))
        .await?
        .json::<f64>()
        .await?;

    if (dydx_price - uni_price) / uni_price > 0.05 {
        // Execute buy-low/sell-high logic
        println!("Arbitrage opportunity: {}% spread", ((dydx_price - uni_price)/uni_price)*100.0);
    }
    Ok(())
}
