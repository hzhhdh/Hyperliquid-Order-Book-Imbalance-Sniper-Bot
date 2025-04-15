import time
import threading
from order_executor import execute_preemptive_order
from config import CONFIG

def twap_order_execution():
    total_amount = CONFIG["TRADE_AMOUNT"]
    slices = CONFIG["TWAP_SLICES"]
    interval = CONFIG["TWAP_INTERVAL"]
    slice_amount = total_amount // slices

    # Set minimum order size if not already set:
    if not CONFIG["TWAP_MIN_ORDER_SIZE"]:
        CONFIG["TWAP_MIN_ORDER_SIZE"] = slice_amount

    print(f"Executing TWAP: {slices} slices, each {slice_amount} wei, every {interval} seconds.")
    for i in range(slices):
        print(f"TWAP slice {i+1}/{slices} executing...")
        original_amount = CONFIG["TRADE_AMOUNT"]
        CONFIG["TRADE_AMOUNT"] = slice_amount  # Temporarily override
        execute_preemptive_order()
        CONFIG["TRADE_AMOUNT"] = original_amount
        time.sleep(interval)

def start_twap_module():
    if CONFIG["TWAP_ENABLE"]:
        twap_thread = threading.Thread(target=twap_order_execution)
        twap_thread.start()
    else:
        print("TWAP module disabled; executing single order.")
        execute_preemptive_order()

if __name__ == "__main__":
    start_twap_module()
