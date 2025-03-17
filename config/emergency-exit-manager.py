class EmergencyExitManager:  
    def __init__(self):  
        self.fallback_exchanges = ["bybit", "okx", "kucoin"]  

    def execute_emergency_close(self, position_id: str):  
        main_order = HyperliquidAPI().cancel_order(position_id)  
        if not main_order["success"]:  
            for exchange in self.fallback_exchanges:  
                if self._hedge_on_cex(position_id, exchange):  
                    break  

    def _hedge_on_cex(self, position_id: str, exchange: str) -> bool:  
        """Открывает противоположную позицию на CEX"""  
        try:  
            pos = HyperliquidAPI().get_position(position_id)  
            cex = CCXT(exchange).create_market_order(  
                symbol=pos["symbol"],  
                side: "sell" if pos["side"] == "long" else "buy",  
                amount: pos["amount"]  
            )  
            return cex["filled"] == pos["amount"]  
        except Exception:  
            return False  
