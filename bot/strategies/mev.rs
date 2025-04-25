use ethers::{prelude::*, providers::Provider};
use flashbots::FlashbotsMiddleware;

async fn mev_protected_swap(provider: Provider<Http>, signer: LocalWallet) {
    let fb = FlashbotsMiddleware::new(provider, signer, "https://relay.flashbots.net");
    let tx = TransactionRequest::pay("vitalik.eth", 100).gas(21000);
    fb.send_transaction(tx).await.unwrap();
}

