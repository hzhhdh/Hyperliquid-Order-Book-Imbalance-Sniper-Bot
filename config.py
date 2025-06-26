import json

def load_config() -> dict:
    """Load configuration from config.json."""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "telegram_token": "",
            "telegram_chat_id": "",
            "bitquery_api_key": "",
            "snipe_amount": 0.1,
            "wallet": {"public_key": "", "private_key": ""}
        }
