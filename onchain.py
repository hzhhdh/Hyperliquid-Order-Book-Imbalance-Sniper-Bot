"""Module for on-chain Bitcoin analytics."""
import requests
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class OnChainAnalyzer:
    """Class to analyze Bitcoin blockchain data."""
    def __init__(self, config: Dict, settings: Dict):
        self.node_url = config["node"]["url"]
        self.metrics = settings["onchain"]["metrics"]
        self.exchanges = settings["onchain"]["exchanges"]
        self.session = requests.Session()

    def fetch_onchain_data(self, metric: str) -> Dict:
        """Fetch on-chain data for a specific metric."""
        try:
            endpoint = f"{self.node_url}/metrics/{metric}"
            response = self.session.get(endpoint)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Failed to fetch {metric} data: {e}")
            return {}

    def analyze_whale_movements(self) -> List[Dict]:
        """Analyze large transactions between wallets or exchanges."""
        whale_txs = []
        for exchange in self.exchanges:
            data = self.fetch_onchain_data(f"exchange_flow/{exchange}")
            for tx in data.get("transactions", []):
                amount = tx.get("value", 0) / 1e8
                if amount >= 100:  # Whale threshold
                    whale_txs.append({"exchange": exchange, "amount": amount})
        return whale_txs

    def start_analysis(self):
        """Start continuous on-chain analysis."""
        logger.info("Starting on-chain analysis")
        for metric in self.metrics:
            data = self.fetch_onchain_data(metric)
            if data:
                logger.info(f"Fetched {metric}: {data}")
        whales = self.analyze_whale_movements()
        for whale in whales:
            logger.info(f"Whale movement: {whale['amount']} BTC on {whale['exchange']}")
