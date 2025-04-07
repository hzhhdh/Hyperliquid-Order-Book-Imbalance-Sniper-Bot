import time
import logging

logger = logging.getLogger(__name__)

class RiskManager:
    def __init__(self, portfolio_value, stop_loss_pct, trailing_stop_pct):
        """
        Initialize the Risk Manager.
        :param portfolio_value: Total portfolio capital.
        :param stop_loss_pct: Fixed stop loss as a decimal (e.g., 0.05 for 5%).
        :param trailing_stop_pct: Trailing stop threshold as a decimal.
        """
        self.portfolio_value = portfolio_value
        self.stop_loss_pct = stop_loss_pct
        self.trailing_stop_pct = trailing_stop_pct
        self.entry_prices = {}  # {symbol: entry price}
        self.high_prices = {}   # {symbol: highest observed price}

    def set_entry(self, symbol, price):
        """Record the entry price for a symbol."""
        self.entry_prices[symbol] = price
        self.high_prices[symbol] = price
        logger.info(f"Set entry for {symbol} at {price}")

    def update_price(self, symbol, current_price):
        """Update the highest price observed for a symbol."""
        if symbol in self.high_prices and current_price > self.high_prices[symbol]:
            self.high_prices[symbol] = current_price
            logger.info(f"Updated high price for {symbol}: {current_price}")

    def check_stop_loss(self, symbol, current_price):
        """
        Check if the fixed stop loss is breached.
        :return: True if stop loss should trigger.
        """
        entry_price = self.entry_prices.get(symbol)
        if entry_price is None:
            return False
        if (entry_price - current_price) / entry_price >= self.stop_loss_pct:
            logger.warning(f"Stop loss triggered for {symbol} at price {current_price}")
            return True
        return False

    def check_trailing_stop(self, symbol, current_price):
        """
        Check if the trailing stop condition is met.
        :return: True if trailing stop should trigger.
        """
        high_price = self.high_prices.get(symbol)
        if high_price is None:
            return False
        if (high_price - current_price) / high_price >= self.trailing_stop_pct:
            logger.warning(f"Trailing stop triggered for {symbol} at price {current_price}")
            return True
        return False

if __name__ == "__main__":
    rm = RiskManager(portfolio_value=200000, stop_loss_pct=0.05, trailing_stop_pct=0.02)
    rm.set_entry("ETH", 2000)
    test_prices = [2000, 2050, 2100, 2080, 2060, 2020]
    for price in test_prices:
        rm.update_price("ETH", price)
        if rm.check_stop_loss("ETH", price):
            print(f"Stop loss triggered at {price}")
        if rm.check_trailing_stop("ETH", price):
            print(f"Trailing stop triggered at {price}")
