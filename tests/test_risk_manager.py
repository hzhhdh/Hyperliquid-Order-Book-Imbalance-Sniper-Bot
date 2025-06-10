import unittest
from src.core.risk_manager import RiskManager
from src.utils.config import load_config

class TestRiskManager(unittest.TestCase):
    def setUp(self):
        self.config = load_config()
        self.risk_manager = RiskManager(self.config['risk'])

    def test_evaluate_trade(self):
        trade = {'amount': 100, 'capital': 1000}
        market_data = {'volatility': 3.0}
        approved, message = self.risk_manager.evaluate_trade(trade, market_data)
        self.assertTrue(approved)

if __name__ == '__main__':
    unittest.main()
