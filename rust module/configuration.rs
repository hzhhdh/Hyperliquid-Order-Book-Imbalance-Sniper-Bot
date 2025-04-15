pub mod config {
    use serde::{Deserialize, Serialize};

    /// The AppConfig struct stores all adjustable parameters.
    /// In a production environment, this might be loaded from a JSON/YAML file.
    #[derive(Debug, Serialize, Deserialize, Clone)]
    pub struct AppConfig {
        // General Trading Settings
        pub capital: u64, // Capital in USD (e.g., 100000)
        pub your_address: String, // Public wallet address
        pub private_key: String,  // WARNING: In production, load securely!

        // Network Parameters
        pub rpc_provider_url: String,
        pub filter_type: String,
        pub poll_interval: f64, // in seconds

        // Multi-Network & Custom RPC
        pub available_networks: std::collections::HashMap<String, String>,
        pub custom_rpc_endpoints: std::collections::HashMap<String, String>,
        pub selected_network: String,

        // Token Selection: Buy token & Target token
        pub buy_token_address: String,
        pub target_token_address: String,

        // DEX Selection: Map of DEX names to router details
        pub available_dexes: std::collections::HashMap<String, DexInfo>,
        pub selected_dex: String,

        // Mempool/Filtering
        pub whale_threshold_value: u128, // Threshold in Wei (e.g., 5 ETH = 5 * 10^18)
        pub target_function_identifier: String,
        pub slippage_tolerance_factor: f64,
        pub address_whitelist: Vec<String>,
        pub address_blacklist: Vec<String>,

        // Signal Generation Parameters
        pub signal_cooldown_period: f64, // seconds
        pub verification_delay_threshold: u64, // milliseconds

        // Order Execution Parameters
        pub trade_amount: u128, // in Wei (e.g., 0.5 ETH)
        pub gas_limit: u64,
        pub gas_premium_multiplier: f64,
        pub transaction_deadline_offset: u64, // seconds

        // TWAP (Time-Weighted Average Price) Strategy Options
        pub twap_enable: bool,
        pub twap_slices: u32,
        pub twap_interval: u64, // seconds between slices
        pub twap_min_order_size: Option<u128>, // Optional: calculated dynamically

        // Risk Management Settings
        pub stop_loss_level: f64,      // e.g., 0.90 (10% drop)
        pub take_profit_level: f64,    // e.g., 1.20 (20% profit)
        pub trailing_stop_distance: f64,  // e.g., 0.95 (5% trailing stop)

        // Logging & Monitoring
        pub log_level: String,
        pub polling_interval_for_metrics: f64, // seconds
        pub max_retry_attempts: u32,

        // Network Congestion / Environment
        pub network_congestion_threshold: u64,  // e.g., gas price in Gwei threshold
    }

    impl Default for AppConfig {
        fn default() -> Self {
            use std::collections::HashMap;
            let mut networks = HashMap::new();
            networks.insert("Ethereum".to_string(), "https://mainnet.infura.io/v3/YOUR_INFURA_KEY".to_string());
            networks.insert("Binance Smart Chain".to_string(), "https://bsc-dataseed.binance.org/".to_string());
            networks.insert("Polygon".to_string(), "https://polygon-rpc.com/".to_string());
            networks.insert("Arbitrum".to_string(), "https://arb1.arbitrum.io/rpc".to_string());
            networks.insert("Avalanche".to_string(), "https://api.avax.network/ext/bc/C/rpc".to_string());
            networks.insert("Optimism".to_string(), "https://mainnet.optimism.io".to_string());

            let available_dexes = {
                let mut dexes = HashMap::new();
                dexes.insert("Uniswap".to_string(), super::dex_loader::DexInfo {
                    router_address: "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D".to_string(),
                    abi_file: "UniswapV2RouterABI.json".to_string(),
                });
                dexes.insert("SushiSwap".to_string(), super::dex_loader::DexInfo {
                    router_address: "0xd9e1ce17f2641f24aE83637ab66a2cca9C378B9F".to_string(),
                    abi_file: "SushiSwapRouterABI.json".to_string(),
                });
                dexes
            };

            Self {
                capital: 100_000,
                your_address: "0xYourHighValueWalletAddress".to_string(),
                private_key: "YOUR_PRIVATE_KEY".to_string(),

                rpc_provider_url: "https://mainnet.infura.io/v3/YOUR_INFURA_KEY".to_string(),
                filter_type: "pending".to_string(),
                poll_interval: 1.0,

                available_networks: networks,
                custom_rpc_endpoints: HashMap::new(),
                selected_network: "Ethereum".to_string(),

                buy_token_address: "0xC02aaa39b223FE8D0a0e5C4F27eAD9083C756Cc2".to_string(),
                target_token_address: "0xTokenAddressToSnipe".to_string(),

                available_dexes,
                selected_dex: "Uniswap".to_string(),

                whale_threshold_value: 5 * 10u128.pow(18), // 5 ETH in Wei
                target_function_identifier: "swapExactETHForTokens".to_string(),
                slippage_tolerance_factor: 0.95,
                address_whitelist: vec![],
                address_blacklist: vec![],

                signal_cooldown_period: 1.0,
                verification_delay_threshold: 200,

                trade_amount: (0.5 * 10f64.powi(18)) as u128, // 0.5 ETH in Wei
                gas_limit: 300_000,
                gas_premium_multiplier: 1.10,
                transaction_deadline_offset: 60,

                twap_enable: true,
                twap_slices: 5,
                twap_interval: 60,
                twap_min_order_size: None,

                stop_loss_level: 0.90,
                take_profit_level: 1.20,
                trailing_stop_distance: 0.95,

                log_level: "DEBUG".to_string(),
                polling_interval_for_metrics: 1.0,
                max_retry_attempts: 3,

                network_congestion_threshold: 150 * 10u64.pow(9), // 150 Gwei threshold
            }
        }
    }
}

pub use config::AppConfig;
