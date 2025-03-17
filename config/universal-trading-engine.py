class MultiLeverageTrader:  
    def execute_trade(self, coin: str, direction: str, strategy: dict):  
        leverage = self._get_leverage(coin, strategy["leverage_rules"])  
        amount = self._calculate_position_size(coin, leverage)  
        order = self._place_order(coin, direction, amount, leverage)  
        self._start_safety_monitor(order["id"], strategy["exit_rules"])  

    def _get_leverage(self, coin: str, rules: dict) -> int:  
        """Применяет правила выбора плеча"""  
        if rules["type"] == "volatility_based":  
            volatility = VolatilityOracle.get(coin, "1h")  
            return AdaptiveLeverageManager().calculate_leverage(coin, volatility)  
        elif rules["type"] == "fixed":  
            return rules["value"]  

    def _place_order(self, coin: str, side: str, amount: float, leverage: int):  
        try:  
            return HyperliquidAPI().create_order(  
                symbol=coin,  
                type="limit" if leverage > 50 else "market",  
                side=side,  
                amount=amount,  
                params={  
                    "leverage": leverage,  
                    "reduceOnly": False,  
                    "timeInForce": "GTC"  
                }  
            )  
        except MarginError:  
            self._auto_add_collateral(coin, amount * 0.1)  # Автопополнение маржи  
