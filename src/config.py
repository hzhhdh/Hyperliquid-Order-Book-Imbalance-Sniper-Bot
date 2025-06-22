"""Module for loading configuration and settings."""
import json
import yaml
import logging
from cryptography.fernet import Fernet
from typing import Dict

logger = logging.getLogger(__name__)

def load_config(config_path: str) -> Dict:
    """Load and decrypt configuration file."""
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        # Decrypt sensitive fields (placeholder for demo)
        key = Fernet.generate_key()  # In production, store securely
        cipher = Fernet(key)
        if "binance" in config["exchanges"]:
            config["exchanges"]["binance"]["api_key"] = cipher.decrypt(
                config["exchanges"]["binance"]["api_key"].encode()
            ).decode()
        return config
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        raise

def load_settings(settings_path: str) -> Dict:
    """Load settings file."""
    try:
        with open(settings_path, "r") as f:
            settings = yaml.safe_load(f)
        return settings
    except Exception as e:
        logger.error(f"Failed to load settings: {e}")
        raise
