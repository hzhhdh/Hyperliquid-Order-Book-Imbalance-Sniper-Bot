def manage_stop_loss_take_profit(entry_price, current_price, stop_loss_pct, take_profit_pct):
    """Manage stop-loss and take-profit levels."""
    stop_loss_price = entry_price * (1 + stop_loss_pct)
    take_profit_price = entry_price * (1 + take_profit_pct)
    
    if current_price <= stop_loss_price:
        return "sell", "Stop-loss triggered"
    elif current_price >= take_profit_price:
        return "sell", "Take-profit triggered"
    return "hold", ""
