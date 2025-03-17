from decimal import Decimal
from typing import Optional
import numpy as np

class RiskManager:
    """
    Dynamic risk calculation engine for position management.
    Implements volatility-based leverage adjustments.
    """
    
    def __init__(self, max_leverage: int = 20):
        self.max_leverage = max_leverage
        self.volatility_window = 24 * 60  # 24 hours in minutes
        
    def calculate_adjusted_leverage(
        self, 
        price_data: list[float], 
        current_leverage: int
    ) -> int:
        """
        Adjust leverage based on price volatility (STD).
        
        Args:
            price_data: Last 24h price series
            current_leverage: Current position leverage
            
        Returns:
            Adjusted leverage (1-20x)
        """
        if len(price_data) < 2:
            return current_leverage
            
        returns = np.diff(price_data) / price_data[:-1]
        volatility = np.std(returns) * 100  # in %
        
        if volatility > 5.0:
            return max(1, current_leverage - 2)
        return min(self.max_leverage, current_leverage + 1)
