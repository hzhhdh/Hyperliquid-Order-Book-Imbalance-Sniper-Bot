use ethers::prelude::*;

pub struct MEVShield {
    private_rpc: String,
    max_priority_fee: u64,
}

impl MEVShield {
    pub fn new(rpc: String) -> Self {
        MEVShield { 
            private_rpc: rpc,
            max_priority_fee: 3_000_000_000, // 3 Gwei default
        }
    }

    pub async fn send_private_tx(&self, tx: TransactionRequest) -> Result<TxHash, ProviderError> {
        let provider = Provider::<Http>::connect(&self.private_rpc).await;
        provider.send_transaction(tx, None).await
    }
}
