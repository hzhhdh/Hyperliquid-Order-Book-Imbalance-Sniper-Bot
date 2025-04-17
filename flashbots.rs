use ethers::prelude::*;
use std::convert::TryFrom;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let provider = Provider::<Http>::try_from("https://mainnet.infura.io/v3/YOUR_INFURA_KEY")?;
    let wallet: LocalWallet = "0xYOUR_PRIVATE_KEY".parse()?;
    let client = SignerMiddleware::new(provider.clone(), wallet.clone());
    
    // Bundle two simple ETH transfers
    let tx1 = TransactionRequest::pay("0xAbC1230000000000000000000000000000000000", parse_ether(0.1)?);
    let tx2 = TransactionRequest::pay("0xDef4560000000000000000000000000000000000", parse_ether(0.2)?);

    // Sign transactions
    let signed1 = wallet.sign_transaction(&tx1).await?;
    let signed2 = wallet.sign_transaction(&tx2).await?;

    // Submit bundle via Flashbots
    let flashbots = FlashbotsMiddleware::new(
        provider.clone(),
        "https://relay.flashbots.net",
        wallet
    );
    let bundle = vec![signed1, signed2];
    let pending = flashbots.send_bundle(&bundle, None::<u64>).await?;
    println!("Bundle submitted: {:?}", pending.bundle_hash);
    Ok(())
}
