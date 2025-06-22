"""Utility functions for Royen Bitcoin Analytic."""
import logging
from typing import Any

logger = logging.getLogger(__name__)

def validate_btc_amount(amount: float) -> bool:
    """Validate Bitcoin amount."""
    if not isinstance(amount, (int, float)) or amount < 0:
        logger.error(f"Invalid BTC amount: {amount}")
        return False
    return True

def format_btc(amount: float) -> str:
    """Format BTC amount for display."""
    return f"{amount:.8f} BTC"
