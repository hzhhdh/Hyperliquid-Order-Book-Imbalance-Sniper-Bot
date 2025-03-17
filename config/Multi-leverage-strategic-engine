class AdaptiveLeverageManager:  
    def __init__(self):  
        self.min_leverage = 20  
        self.max_leverage = 100  
        self.current_leverage = {}  # {coin: current_leverage}  

    def calculate_leverage(self, coin: str, volatility: float) -> int:  
        """  
        Dynamically selects leverage based on volatility: 
        - With volatility <5%: max_leverage (100x)  
        - With volatility >15%: min_leverage (20x)  
        """  
        leverage = round(  
            self.max_leverage - (volatility - 5) * (self.max_leverage - self.min_leverage) / 10  
        )  
        self.current_leverage[coin] = clamp(leverage, self.min_leverage, self.max_leverage)  
        return self.current_leverage[coin]  

    def get_allowed_coins(self) -> list:  
        """Filters coins with available leverage >=20x"""  
        markets = HyperliquidAPI().fetch_markets()  
        return [  
            m["symbol"] for m in markets  
            if m["maxLeverage"] >= self.min_leverage  
            and m["marginType"] == "isolated"  # Для безопасности  
        ]  
