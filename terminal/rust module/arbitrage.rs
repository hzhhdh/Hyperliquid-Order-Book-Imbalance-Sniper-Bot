use std::collections::HashMap;

pub struct ArbitrageEngine {
    dex_prices: HashMap<String, f64>,
    cex_prices: HashMap<String, f64>,
}

impl ArbitrageEngine {
    pub fn new() -> Self {
        Self {
            dex_prices: HashMap::new(),
            cex_prices: HashMap::new(),
        }
    }

    pub fn check_arbitrage(&self, pair: &str) -> Option<f64> {
        let dex_price = self.dex_prices.get(pair)?;
        let cex_price = self.cex_prices.get(pair)?;
        let spread = (cex_price - dex_price) / dex_price;
        if spread > 0.01 {
            Some(spread)
        } else {
            None
        }
    }
}
