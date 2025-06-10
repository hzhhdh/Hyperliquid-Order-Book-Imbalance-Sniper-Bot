import unittest
from src.core.exchange import Exchange
from src.core.arbitrage import Arbitrage
from src.utils.config import load_config

class TestArbitrage(unittest.TestCase):
    def setUp(self):
        self.config = load_config()
        self.exchange = Exchange(self.config)
        self.arbitrage = Arbitrage(self.exchange, self.config['arbitrage'])

    def test_find_opportunities(self):
        opportunities = self.arbitrage.find_opportunities(['ETH/USDT'])
        self.assertIsInstance(opportunities, list)

if __name__ == '__main__':
    unittest.main()
