import unittest
from src.core.exchange import Exchange
from src.core.order_manager import OrderManager
from src.utils.config import load_config

class TestOrderManager(unittest.TestCase):
    def setUp(self):
        self.config = load_config()
        self.exchange = Exchange(self.config)
        self.order_manager = OrderManager(self.exchange)

    def test_place_order(self):
        order = self.order_manager.place_order('binance', 'ETH/USDT', 1.0, 'market')
        self.assertEqual(order['status'], 'placed')

if __name__ == '__main__':
    unittest.main()
