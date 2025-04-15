pub mod token_selector {
    use super::config::AppConfig;

    pub fn set_buy_token(config: &mut AppConfig, token_address: &str) {
        config.buy_token_address = token_address.to_string();
        println!("Buy token set to: {}", token_address);
    }

    pub fn set_target_token(config: &mut AppConfig, token_address: &str) {
        config.target_token_address = token_address.to_string();
        println!("Target token set to: {}", token_address);
    }
}
