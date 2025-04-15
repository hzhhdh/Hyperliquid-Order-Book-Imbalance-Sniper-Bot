from config import CONFIG

def check_stop_loss(current_price, entry_price):
    if current_price <= entry_price * CONFIG["STOP_LOSS_LEVEL"]:
        print("Stop-Loss condition met.")
        return True
    return False

def check_take_profit(current_price, entry_price):
    if current_price >= entry_price * CONFIG["TAKE_PROFIT_LEVEL"]:
        print("Take-Profit condition met.")
        return True
    return False

def check_trailing_stop(high_price, current_price):
    if current_price <= high_price * CONFIG["TRAILING_STOP_DISTANCE"]:
        print("Trailing Stop condition met.")
        return True
    return False

if __name__ == "__main__":
    # Test with sample prices
    entry = 1000
    current = 850  # 15% drop triggers stop loss (if STOP_LOSS_LEVEL is 0.90)
    check_stop_loss(current, entry)
