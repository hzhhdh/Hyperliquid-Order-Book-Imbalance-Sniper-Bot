import threading
import time
from main import main_loop
from dynamic_config import update_gas_premium, toggle_twap
from loader import load_config

def initialize_bot():
    # Load custom configuration if available
    load_config()
    # Optionally adjust parameters based on command-line input or config interface:
    # update_gas_premium(1.15)
    # toggle_twap(True)
    print("Bot initialized with the following configuration:")
    for key, value in load_config().items():
        print(f"  {key}: {value}")

def run():
    initialize_bot()
    try:
        main_loop()
    except Exception as e:
        print("Bot encountered a critical error and will now exit.")
        raise e

if __name__ == "__main__":
    run()
