pub mod dex_loader {
    use super::config::AppConfig;
    use serde::{Deserialize, Serialize};

    #[derive(Debug, Serialize, Deserialize, Clone)]
    pub struct DexInfo {
        pub router_address: String,
        pub abi_file: String,
    }

    pub fn load_dex_info(config: &AppConfig) -> DexInfo {
        config.available_dexes
            .get(&config.selected_dex)
            .expect("Selected DEX not found in configuration")
            .clone()
    }
}
