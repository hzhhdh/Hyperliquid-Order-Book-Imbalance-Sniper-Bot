class ConfigManager:
    def __init__(self):
        self.config = {
            "ethereum_rpc": "wss://eth-mainnet.alchemyapi.io/v2/...",
            "solana_rpc": "https://api.mainnet-beta.solana.com",
            "api_keys": {"certik": "...", "x": "..."}
        }

    def get_config(self, key: str) -> str:
        return self.config.get(key, "")
