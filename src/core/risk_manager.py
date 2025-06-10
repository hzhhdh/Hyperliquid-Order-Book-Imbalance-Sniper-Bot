class RiskManager:
    def __init__(self, config: dict):
        self.stop_loss = config.get('stop_loss', 2.0)  # % loss
        self.take_profit = config.get('take_profit', 5.0)  # % profit
        self.max_allocation = config.get('max_allocation', 10.0)  # % of capital
        self.volatility_threshold = config.get('volatility_threshold', 5.0)  # % change

    def evaluate_trade(self, trade, market_data):
        if market_data['volatility'] > self.volatility_threshold:
            return False, "High volatility detected"
        if trade['amount'] > self.max_allocation * trade['capital'] / 100:
            return False, "Exceeds max allocation"
        return True, "Trade approved"
