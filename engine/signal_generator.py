import time
from order_executor import execute_preemptive_order
from config import CONFIG

_last_signal_time = 0

def signal_preemptive_buy(tx):
    global _last_signal_time
    now = time.time()
    if now - _last_signal_time >= CONFIG["SIGNAL_COOLDOWN_PERIOD"]:
        _last_signal_time = now
        print("Signal: Whale buy order detected. Triggering preemptive order.")
        execute_preemptive_order()
    else:
        print("Signal ignored due to cooldown period.")
