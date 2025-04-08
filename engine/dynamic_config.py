from loader import update_config

def update_gas_premium(new_multiplier: float):
    update_config("GAS_PREMIUM_MULTIPLIER", new_multiplier)

def update_whale_threshold(new_threshold: int):
    update_config("WHALE_THRESHOLD_VALUE", new_threshold)

def toggle_twap(enable: bool):
    update_config("TWAP_ENABLE", enable)

# Additional functions can be added for adjusting any parameter dynamically.
