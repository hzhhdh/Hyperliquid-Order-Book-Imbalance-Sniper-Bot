pub struct StakingPosition {
    pub collateral: f64,
    pub leverage: f64,
    pub liquidation_price: f64,
}

impl StakingPosition {
    pub fn new(collateral: f64, leverage: f64) -> Self {
        Self {
            collateral,
            leverage,
            liquidation_price: collateral * 0.8 / leverage,
        }
    }
}
