from core.strategy import Strategy

class DataSyncStrategy(Strategy):
    """
    Polls wallets and exchanges at configurable
    intervals and updates local DB.
    """
    def __init__(self, interval_sec: int):
        self.interval = interval_sec

    def execute(self):
        # Schedule and perform sync
        pass
