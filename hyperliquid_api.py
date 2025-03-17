import ccxt
from typing import Dict, Any
from .config import config

class HyperLiquidAPI:
    def __init__(self):
        self.exchange = ccxt.hyperliquid({
            'apiKey': config.HYPERLIQUID_API_KEY.get_secret_value(),
            'secret': config.HYPERLIQUID_API_SECRET.get_secret_value(),
            'enableRateLimit': True
        })
    
    def get_position(self, symbol: str) -> Dict[str, Any]:
        """Fetch current position for given symbol"""
        try:
            positions = self.exchange.fetch_positions([symbol])
            return next(
                (p for p in positions if p['symbol'] == symbol), 
                None
            )
        except ccxt.NetworkError as e:
            self._handle_api_error(e)
