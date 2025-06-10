import unittest
from src.core.exchange import Exchange
from src.utils.config import load_config

class TestExchange(unittest.TestCase):
    def setUp(self):
        self.config = load_config()
        self.exchange = Exchange(self.config)

    def test_fetch_price(self):
        # Placeholder test (requires real API keys for actual testing)
        self.assertIsInstance(self.exchange.fetch_price('binance', 'ETH/USDT'), float)

if __name__ == '__main__':
    unittest.main()
