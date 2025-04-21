from core.strategy import Strategy

class PortfolioVaRStrategy(Strategy):
    """
    Computes Value‑at‑Risk via Monte Carlo
    at configured confidence levels.
    """
    def __init__(self, confidence_level: float, horizon_days: int):
        self.confidence_level = confidence_level
        self.horizon_days = horizon_days

    def execute(self, returns: list) -> float:
        # Run MC simulation, return VaR
        pass
