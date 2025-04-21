import time
from threading import Thread

class DataSyncService:
    """Background task to keep local DB synchronized."""
    def __init__(self, connectors: list, interval: int = 60):
        self.connectors = connectors
        self.interval = interval

    def start(self):
        def _run():
            while True:
                for c in self.connectors:
                    c.get_balances()
                time.sleep(self.interval)
        Thread(target=_run, daemon=True).start()
