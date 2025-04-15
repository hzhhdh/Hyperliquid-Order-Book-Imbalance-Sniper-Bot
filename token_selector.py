from config import CONFIG

def select_buy_token(token_address: str):
    CONFIG["BUY_TOKEN_ADDRESS"] = token_address
    print(f"Buy token updated to: {token_address}")

def select_target_token(token_address: str):
    CONFIG["TARGET_TOKEN_ADDRESS"] = token_address
    print(f"Target token updated to: {token_address}")

# For testing:
if __name__ == "__main__":
    select_buy_token("0xNewBuyTokenAddressExample...")
    select_target_token("0xNewTargetTokenAddressExample...")
