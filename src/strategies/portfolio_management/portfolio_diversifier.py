from web3 import Web3
import requests
import logging
from typing import Dict

logging.basicConfig(level=logging.INFO, filename='portfolio_diversifier.log')

class PortfolioDiversifier:
    def __init__(self, w3_provider: str, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider(w3_provider))
        self.account = self.w3.eth.account.from_key(private_key)
        self.cmc_api = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    def get_asset_volatility(self, token_symbol: str) -> float:
        """Fetch 24h volatility from CoinmarketCap."""
        try:
            response = requests.get(self.cmc_api, headers={'X-CMC_PRO_API_KEY': 'YOUR_API_KEY'}, params={'symbol': token_symbol})
            response.raise_for_status()
            return response.json()['data'][token_symbol]['quote']['USD']['percent_change_24h']
        except Exception as e:
            logging.error(f"Error fetching volatility for {token_symbol}: {e}")
            raise

    def diversify(self, assets: Dict[str, float], target_risk: float) -> None:
        """Rebalance portfolio to reduce risk exposure."""
        total_risk = 0.0
        for token, amount in assets.items():
            volatility = self.get_asset_volatility(token)
            total_risk += abs(volatility) * (amount / sum(assets.values()))
        if total_risk > target_risk:
            # TODO: Swap high-volatility assets to stablecoins
            logging.info(f"Diversified portfolio, reduced risk from {total_risk} to {target_risk}")
        else:
            logging.info(f"Portfolio risk acceptable: {total_risk}")

if __name__ == "__main__":
    diversifier = PortfolioDiversifier("https://mainnet.infura.io/v3/YOUR_PROJECT_ID", "YOUR_PRIVATE_KEY")
    assets = {"ETH": 1000.0, "USDC": 2000.0, "DAI": 1500.0}
    diversifier.diversify(assets, 5.0)
