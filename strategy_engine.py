import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

class BaseStrategy:
    def __init__(self, data, **params):
        """
        Base class for all trading strategies.
        :param data: Pandas DataFrame with market data.
        :param params: Strategy-specific parameters.
        """
        self.data = data
        self.params = params

    def generate_signals(self):
        """
        Must be overridden by subclass. Generates trading signals.
        :return: DataFrame with signals.
        """
        raise NotImplementedError("Subclasses must implement generate_signals()")

class TrendFollowingStrategy(BaseStrategy):
    def generate_signals(self):
        """
        Implements a moving average crossover strategy.
        Customizable parameters: short_window, long_window.
        :return: DataFrame with 'signal' column: 1 for buy, -1 for sell.
        """
        short_window = self.params.get('short_window', 20)
        long_window = self.params.get('long_window', 50)

        signals = pd.DataFrame(index=self.data.index)
        signals['price'] = self.data['price']
        signals['short_ma'] = self.data['price'].rolling(window=short_window).mean()
        signals['long_ma'] = self.data['price'].rolling(window=long_window).mean()
        signals['signal'] = np.where(signals['short_ma'] > signals['long_ma'], 1.0, -1.0)
        logger.info("TrendFollowingStrategy signals generated.")
        return signals

# Example usage with dummy data:
if __name__ == "__main__":
    # Create dummy market data
    dates = pd.date_range(start="2023-01-01", periods=100, freq="D")
    prices = pd.Series(np.random.randn(100).cumsum() + 100, index=dates)
    market_data = pd.DataFrame({"price": prices})

    strategy = TrendFollowingStrategy(market_data, short_window=10, long_window=30)
    signals = strategy.generate_signals()
    print(signals.tail())
