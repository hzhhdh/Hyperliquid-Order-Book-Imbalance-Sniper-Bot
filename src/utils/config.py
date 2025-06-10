import json
import os

def load_config(config_file='config/arbify_config.json'):
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    return {
        'infura_url': 'https://mainnet.infura.io/v3/YOUR_INFURA_KEY',
        'cex': {
            'binance': {'api_key': '', 'secret': ''},
            'kraken': {'api_key': '', 'secret': ''}
        },
        'arbitrage': {
            'min_spread': 0.5,
            'max_gas_fee': 10.0
        },
        'risk': {
            'stop_loss': 2.0,
            'take_profit': 5.0,
            'max_allocation': 10.0,
            'volatility_threshold': 5.0
        }
    }
