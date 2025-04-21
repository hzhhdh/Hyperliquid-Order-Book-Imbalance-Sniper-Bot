from core.strategy import Strategy

class PortfolioPnLStrategy(Strategy):
    """
    Calculates realized & unrealized PnL
    using FIFO/LIFO lot accounting.
    """
    def __init__(self, method: str = "FIFO"):
        self.method = method

    def execute(self, transactions: list):
        # Compute cost basis and PnL breakdown
        pass
