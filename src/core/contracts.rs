#[derive(Clone, Debug)]
pub struct PancakeSwap {
    pub router: Address,
    pub factory: Address,
}

impl PancakeSwap {
    pub async fn get_pair(&self, token_a: Address, token_b: Address) -> Result<Address, String> {
        let contract = Contract::from_json(
            self.factory,
            include_bytes!("abis/pancake_factory.json"),
        )?;
        
        contract
            .method::<_, Address>("getPair", (token_a, token_b))
            .unwrap()
            .call()
            .await
            .map_err(|e| format!("Error: {:?}", e))
    }
}
