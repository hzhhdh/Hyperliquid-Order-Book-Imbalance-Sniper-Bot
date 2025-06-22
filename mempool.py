"""Module for monitoring Bitcoin mempool activity."""
import requests
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class MempoolMonitor:
    """Class to monitor Bitcoin mempool transactions."""
    def __init__(self, config: Dict, settings: Dict):
        self.node_url = config["node"]["url"]
        self.filters = settings["mempool"]["filters"]
        self.alerts = settings["mempool"]["alerts"]
        self.session = requests.Session()

    def fetch_mempool_data(self) -> Dict:
        """Fetch mempool data from the configured node."""
        try:
            response = self.session.get(f"{self.node_url}/mempool")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch mempool data: {e}")
            return {}

    def filter_transactions(self, transactions: List[Dict]) -> List[Dict]:
        """Filter transactions based on user settings."""
        filtered = []
        for tx in transactions:
            amount = tx.get("value", 0) / 1e8  # Convert satoshis to BTC
            fee_rate = tx.get("fee_rate", 0)  # satoshi/vbyte
            if (amount >= self.filters["min_amount"] and
                fee_rate in self.filters["fee_range"] and
                tx.get("address_type") in self.filters["address_type"]):
                filtered.append(tx)
        return filtered

    def check_alerts(self, transactions: List[Dict]) -> List[str]:
        """Check for transactions triggering alerts."""
        alerts = []
        for tx in transactions:
            amount = tx.get("value", 0) / 1e8
            if amount >= self.alerts["transaction_size"]:
                alerts.append(f"Large transaction detected: {amount} BTC")
        return alerts

    def start_monitoring(self):
        """Start continuous mempool monitoring."""
        logger.info("Starting mempool monitoring")
        data = self.fetch_mempool_data()
        if data:
            transactions = data.get("transactions", [])
            filtered = self.filter_transactions(transactions)
            alerts = self.check_alerts(filtered)
            for alert in alerts:
                logger.info(alert)
