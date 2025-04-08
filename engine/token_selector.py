from config import CONFIG

def select_buy_token(new_address: str):
    CONFIG["BUY_TOKEN_ADDRESS"] = new_address
    print(f"Buy token set to: {new_address}")

def select_target_token(new_address: str):
    CONFIG["TARGET_TOKEN_ADDRESS"] = new_address
    print(f"Target token set to: {new_address}")

# Example usage:
# select_buy_token("0xNewBuyTokenAddress...")
# select_target_token("0xNewTargetTokenAddress...")
