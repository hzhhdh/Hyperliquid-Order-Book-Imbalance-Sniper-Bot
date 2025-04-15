pub mod network {
    use super::config::AppConfig;
    use ethers::providers::{Http, Provider};
    use std::sync::Arc;

    pub fn get_provider(config: &AppConfig) -> Arc<Provider<Http>> {
        // Use custom endpoint if defined
        let rpc_url = if let Some(custom) = config.custom_rpc_endpoints.get(&config.selected_network) {
            custom.clone()
        } else {
            config.available_networks.get(&config.selected_network)
                     .expect("No RPC endpoint found for selected network").clone()
        };
        println!("Connecting to {} network using RPC: {}", config.selected_network, rpc_url);
        let provider = Provider::<Http>::try_from(rpc_url)
            .expect("Failed to connect to RPC endpoint");
        Arc::new(provider)
    }
}
