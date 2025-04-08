def check_stop_loss(current_price, entry_price):
    # If current price falls below the configured percentage (e.g., 10% drop), trigger stop loss.
    if current_price <= entry_price * CONFIG["STOP_LOSS_LEVEL"]:
        print("Stop-Loss triggered.")
        return True
    return False

def check_take_profit(current_price, entry_price):
    # If current price exceeds entry price by the configured percentage (e.g., 20% gain), trigger take profit.
    if current_price >= entry_price * CONFIG["TAKE_PROFIT_LEVEL"]:
        print("Take-Profit triggered.")
        return True
    return False

def check_trailing_stop(current_high, current_price):
    # Check if current price has fallen to trailing stop percentage (e.g., 5% below highest reached)
    if current_price <= current_high * CONFIG["TRAILING_STOP_DISTANCE"]:
        print("Trailing Stop triggered.")
        return True
    return False
