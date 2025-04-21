import requests

class ExchangeAPIConnector:
    """Reads balances and trade history from CEX via REST API."""
    def __init__(self, base_url: str, api_key: str, secret: str):
        self.base_url = base_url
        self.headers = {"X-API-KEY": api_key}
        self.secret = secret

    def get_balances(self):
        resp = requests.get(f"{self.base_url}/api/v3/account", headers=self.headers)
        return resp.json().get("balances", [])
