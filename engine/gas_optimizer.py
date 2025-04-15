from network import w3
from config import CONFIG

def get_premium_gas_price():
    current_gas_price = w3.eth.gasPrice
    premium_price = current_gas_price * CONFIG["GAS_PREMIUM_MULTIPLIER"]
    print(f"Current gas price: {current_gas_price}, Premium gas price: {premium_price}")
    return int(premium_price)

if __name__ == "__main__":
    print("Optimized Gas Price:", get_premium_gas_price())
