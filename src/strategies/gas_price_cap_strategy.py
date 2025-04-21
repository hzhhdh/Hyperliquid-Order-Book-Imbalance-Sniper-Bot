from core.strategy import Strategy

class GasPriceCapStrategy(Strategy):
    """
    Enforces an upper Gwei limit before
    auto‑submitting via private relay.
    """
    def __init__(self, cap_gwei: int):
        self.cap_gwei = cap_gwei

    def execute(self, current_gas: int) -> bool:
        return current_gas <= self.cap_gwei
