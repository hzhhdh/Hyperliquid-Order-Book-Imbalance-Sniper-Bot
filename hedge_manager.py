from ccxt import binance
from .config import config

class HedgeManager:
    """
    Executes emergency hedging on CEX
    when liquidation risk is detected
    """
    
    def __init__(self):
        self.cex = binance({
            'apiKey': config.BINANCE_API_KEY,
            'secret': config.BINANCE_API_SECRET
        })
    
    def execute_flash_hedge(
        self, 
        symbol: str, 
        amount: float, 
        side: str
    ) -> bool:
        """
        Open opposite position on CEX within 3s
        
        Args:
            symbol: Trading pair (BTC/USDT)
            amount: Hedge amount
            side: 'buy' or 'sell'
        """
        try:
            order = self.cex.create_market_order(
                symbol, 
                side, 
                amount
            )
            return order['status'] == 'filled'
        except Exception as e:
            self._send_alert(f"Hedge failed: {str(e)}")
            return False
