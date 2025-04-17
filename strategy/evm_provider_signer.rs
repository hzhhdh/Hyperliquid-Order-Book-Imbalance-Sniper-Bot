async fn setup_provider_and_signer() -> Result<Arc<SignerMiddleware<GasEscalator<Provider<Http>>, LocalWallet>>, Box<dyn std::error::Error>> {
    // Load environment variables
    dotenv::dotenv().ok();
    let rpc_url = std::env::var("ETH_RPC_URL")?;              // Custom RPC endpoint
    let private_key = std::env::var("PRIVATE_KEY")?;          

    // Create HTTP provider
    let provider = Provider::<Http>::try_from(rpc_url)?
        .interval(Duration::from_millis(200u64));           // Polling interval

    // Gas oracle middleware for dynamic gas price
    let gas_oracle = GasOracleMiddleware::new(provider.clone());

    // Gas Escalator middleware to rebroadcast with increasing gas price
    let escalator = GasEscalator::new(gas_oracle, 5, Duration::from_secs(10));

    // Wallet signer
    let wallet: LocalWallet = private_key.parse()?;
    let chain_id = std::env::var("CHAIN_ID")?.parse::<u64>()?;
    let wallet = wallet.with_chain_id(chain_id);

    // Combine provider, middleware, and wallet into a client
    let client = SignerMiddleware::new(escalator, wallet);
    Ok(Arc::new(client))
}
