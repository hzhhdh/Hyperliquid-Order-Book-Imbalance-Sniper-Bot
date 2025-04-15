pub mod loader {
    use super::config::AppConfig;
    use serde_json;
    use std::fs::File;
    use std::io::Read;

    pub fn load_config_from_file(filename: &str) -> AppConfig {
        let mut config = AppConfig::default();
        if let Ok(mut file) = File::open(filename) {
            let mut contents = String::new();
            if let Ok(_) = file.read_to_string(&mut contents) {
                if let Ok(user_config) = serde_json::from_str::<AppConfig>(&contents) {
                    config = user_config;
                    println!("Configuration loaded from {}.", filename);
                } else {
                    println!("Error parsing config file. Using default config.");
                }
            }
        } else {
            println!("Config file not found. Using default configuration.");
        }
        config
    }

    pub fn update_config(config: &mut AppConfig, key: &str, value: &str) {
        // For simplicity, we update a few keys; in production, use a more robust system.
        match key {
            "gas_premium_multiplier" => {
                if let Ok(val) = value.parse::<f64>() {
                    config.gas_premium_multiplier = val;
                }
            },
            "whale_threshold_value" => {
                if let Ok(val) = value.parse::<u128>() {
                    config.whale_threshold_value = val;
                }
            },
            "twap_enable" => {
                if let Ok(val) = value.parse::<bool>() {
                    config.twap_enable = val;
                }
            },
            _ => println!("Key {} update not implemented.", key),
        }
        println!("Updated {} to {}", key, value);
    }
}
