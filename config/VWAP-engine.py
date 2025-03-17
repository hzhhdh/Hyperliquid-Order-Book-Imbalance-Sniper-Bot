class VWAPExecutor:  
    def __init__(self):  
        self.volume_threshold = 0.05  # 5% daily volume  
        self.max_slippage = 0.1       # 0.1% макс. проскальзывание  

    def execute(self, symbol: str, side: str, amount: float):  
        daily_volume = VolumeOracle.get_24h_volume(symbol)  
        max_slice = daily_volume * self.volume_threshold  
        slices = ceil(amount / max_slice)  

        for _ in range(slices):  
            current_volume = self._get_live_volume(symbol)  
            slice_size = min(amount, max_slice * (current_volume / daily_volume))  
            self._place_order(symbol, side, slice_size)  
            amount -= slice_size  

    def _get_live_volume(self, symbol: str) -> float:  
        return HyperliquidAPI().fetch_order_book(symbol)["total_volume"]  
