import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RealTimeUpdater:
    def __init__(self, update_interval=10):
        self.update_interval = update_interval  # Секунды
        self.running = False

    def start_updates(self, fetch_callback):
        self.running = True
        while self.running:
            logging.info("Fetching new data")
            try:
                data = fetch_callback()
                logging.info(f"Updated data: {data}")
            except Exception as e:
                logging.error(f"Update failed: {str(e)}")
            time.sleep(self.update_interval)

    def stop_updates(self):
        self.running = False
        logging.info("Updates stopped")

if __name__ == "__main__":
    def dummy_fetch():
        return {"TVL": 1000000, "Volume": 500000}

    updater = RealTimeUpdater()
    updater.start_updates(dummy_fetch)
