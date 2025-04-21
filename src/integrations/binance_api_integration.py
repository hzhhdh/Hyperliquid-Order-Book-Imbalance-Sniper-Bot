from binance.client import Client

class BinanceAPIIntegration:
    """Connects to Binance for on‑chain/off‑chain data aggregation."""
    def __init__(self, api_key, secret):
        self.client = Client(api_key, secret)

    def get_ticker_price(self, symbol: str):
        return self.client.get_symbol_ticker(symbol=symbol)["price"]
