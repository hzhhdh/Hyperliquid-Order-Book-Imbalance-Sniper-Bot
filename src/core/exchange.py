import ccxt
from web3 import Web3

class Exchange:
    def __init__(self, config):
        self.cex = {}
        self.dex = {}
        self.web3 = Web3(Web3.HTTPProvider(config['infura_url']))
        self.initialize_exchanges(config)

    def initialize_exchanges(self, config):
        # Initialize CEX (Binance, Kraken)
        for exchange_id, credentials in config['cex'].items():
            self.cex[exchange_id] = getattr(ccxt, exchange_id)({
                'apiKey': credentials['api_key'],
                'secret': credentials['secret']
            })
        # Initialize DEX (Uniswap, etc.)
        self.dex['uniswap'] = None  # Placeholder for Uniswap contract

    def fetch_price(self, exchange_id, pair):
        if exchange_id in self.cex:
            ticker = self.cex[exchange_id].fetch_ticker(pair)
            return ticker['last']
        elif exchange_id in self.dex:
            # Placeholder for DEX price fetching
            return 0.0
        raise ValueError(f"Unknown exchange: {exchange_id}")
