"""Module for sending notifications."""
import requests
import logging
from typing import Dict

logger = logging.getLogger(__name__)

class Notifier:
    """Class to send alerts via Telegram, email, or desktop."""
    def __init__(self, config: Dict, settings: Dict):
        self.telegram_config = config["notifications"]["telegram"]
        self.channels = settings["notifications"]["channels"]

    def send_telegram_message(self, message: str):
        """Send a message via Telegram."""
        if not self.telegram_config["enabled"]:
            return
        try:
            bot_token = self.telegram_config["bot_token"]
            chat_id = self.telegram_config["chat_id"]
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            payload = {"chat_id": chat_id, "text": message}
            response = requests.post(url, json=payload)
            response.raise_for_status()
            logger.info(f"Sent Telegram message: {message}")
        except requests.RequestException as e:
            logger.error(f"Failed to send Telegram message: {e}")

    def send_welcome_message(self):
        """Send a welcome message on startup."""
        message = "Royen Bitcoin Analytic started successfully!"
        if "telegram" in self.channels:
            self.send_telegram_message(message)
