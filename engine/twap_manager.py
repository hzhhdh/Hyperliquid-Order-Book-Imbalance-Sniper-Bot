import time
import threading
from order_executor import execute_preemptive_order
from config import CONFIG

def twap_order_execution():
    total_amount = CONFIG["TRADE_AMOUNT"]
    slices = CONFIG["TWAP_SLICES"]
    interval = CONFIG["TWAP_INTERVAL"]
    slice_amount = total_amount // slices
    
    # Set minimum order size if not already set
    if not CONFIG["TWAP_MIN_ORDER_SIZE"]:
        CONFIG["TWAP_MIN_ORDER_SIZE"] = slice_amount

    print(f"Starting TWAP execution: {slices} slices, each of {slice_amount} wei, interval {interval} seconds.")
    for i in range(slices):
        # Prepare to execute each slice:
        print(f"TWAP slice {i+1}/{slices} executing...")
        # Update config TRADE_AMOUNT for this slice temporarily
        original_trade_amount = CONFIG["TRADE_AMOUNT"]
        CONFIG["TRADE_AMOUNT"] = slice_amount
        execute_preemptive_order()
        # Restore original trade amount if needed (depends on architecture)
        CONFIG["TRADE_AMOUNT"] = original_trade_amount
        time.sleep(interval)

def start_twap_module():
    if CONFIG["TWAP_ENABLE"]:
        twap_thread = threading.Thread(target=twap_order_execution)
        twap_thread.start()
    else:
        print("TWAP module is disabled; executing single order.")
        execute_preemptive_order()
