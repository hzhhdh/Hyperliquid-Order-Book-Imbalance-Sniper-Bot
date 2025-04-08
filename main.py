import threading
import time
from mempool_monitor import monitor_mempool
from twap_manager import start_twap_module
from logger import logger
from monitor import display_metrics
from twap_manager import start_twap_module
from order_executor import execute_preemptive_order

def main_loop():
    logger.info("Starting DeFi Sniping Bot with advanced front-running features.")
    # Start monitoring the mempool in a separate thread
    mempool_thread = threading.Thread(target=monitor_mempool, daemon=True)
    mempool_thread.start()

    while True:
        try:
            # Main loop could also poll for risk conditions, update UI, etc.
            # For demo purposes, we simply display performance metrics every POLLING_INTERVAL_FOR_METRICS seconds.
            display_metrics()
            time.sleep(5)  # Adjust refresh interval as needed
        except KeyboardInterrupt:
            logger.info("Shutting down bot due to keyboard interrupt.")
            break
        except Exception as e:
            logger.error(f"Error in main loop: {e}")
          from config import CONFIG

def trigger_order():
    if CONFIG["TWAP_ENABLE"]:
        logger.info("TWAP enabled: Executing order split strategy.")
        start_twap_module()
    else:
        logger.info("TWAP disabled: Executing single preemptive order.")
        execute_preemptive_order()

# You could call trigger_order() from the signal generator as well if desired.

if __name__ == "__main__":
    main_loop()
  
