/// Calculate MACD (Moving Average Convergence Divergence)
pub struct MACD {
    pub macd_line: Vec<f64>,
    pub signal_line: Vec<f64>,
    pub histogram: Vec<f64>,
}

pub fn calculate_macd(prices: &[f64], fast: usize, slow: usize, signal: usize) -> MACD {
    let mut macd_line = vec![0.0; prices.len()];
    let mut signal_line = vec![0.0; prices.len()];
    let mut histogram = vec![0.0; prices.len()];

    let ema_fast = calculate_ema(prices, fast);
    let ema_slow = calculate_ema(prices, slow);

    for i in 0..prices.len() {
        macd_line[i] = ema_fast[i] - ema_slow[i];
    }

    let signal_ema = calculate_ema(&macd_line, signal);
    for i in 0..prices.len() {
        signal_line[i] = signal_ema[i];
        histogram[i] = macd_line[i] - signal_line[i];
    }

    MACD { macd_line, signal_line, histogram }
}

fn calculate_ema(prices: &[f64], period: usize) -> Vec<f64> {
    let mut ema = vec![0.0; prices.len()];
    let k = 2.0 / (period as f64 + 1.0);
    ema[0] = prices[0];

    for i in 1..prices.len() {
        ema[i] = prices[i] * k + ema[i - 1] * (1.0 - k);
    }
    ema
}
