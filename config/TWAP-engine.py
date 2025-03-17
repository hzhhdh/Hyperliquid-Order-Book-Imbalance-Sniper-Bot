class TWAPExecutor:  
    def __init__(self):  
        self.total_duration = 3600  # 1 час (по умолчанию)  
        self.slices = 12            # 12 интервалов по 5 минут  

    def execute(self, symbol: str, side: str, total_amount: float):  
        slice_size = total_amount / self.slices  
        interval = self.total_duration / self.slices  

        for _ in range(self.slices):  
            order = self._place_order(symbol, side, slice_size)  
            self._log_order(order)  
            sleep(interval)  

    def _place_order(self, symbol: str, side: str, amount: float):  
        return HyperliquidAPI().create_order(  
            symbol=symbol,  
            type="limit",  
            side=side,  
            amount=amount,  
            params={"timeInForce": "GTC"}  
        )  
