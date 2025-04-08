from network import w3
from config import CONFIG

def get_premium_gas_price():
    current_gas_price = w3.eth.gasPrice
    premium = current_gas_price * CONFIG["GAS_PREMIUM_MULTIPLIER"]
    print(f"Current gas: {current_gas_price}, premium gas: {premium}")
    return int(premium)
