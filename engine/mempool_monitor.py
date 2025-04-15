import time
from config import CONFIG
from network import w3
from transaction_decoder import decode_tx_input
from signal_generator import signal_preemptive_buy

def monitor_mempool():
    pending_filter = w3.eth.filter(CONFIG["FILTER_TYPE"])
    print("Started monitoring mempool...")
    while True:
        try:
            new_tx_hashes = pending_filter.get_new_entries()
            for tx_hash in new_tx_hashes:
                tx = w3.eth.getTransaction(tx_hash)
                if tx and is_large_buy_order(tx):
                    signal_preemptive_buy(tx)
            time.sleep(CONFIG["POLL_INTERVAL"])
        except Exception as e:
            print(f"Error in mempool monitoring: {e}")

def is_large_buy_order(tx):
    try:
        func_obj, params = decode_tx_input(tx.input)
        if func_obj.function_identifier == CONFIG["TARGET_FUNCTION_IDENTIFIER"]:
            # Check if the swap involves our target token
            if params.get("path", []) and params["path"][-1].lower() == CONFIG["TARGET_TOKEN_ADDRESS"].lower():
                if tx.value >= CONFIG["WHALE_THRESHOLD_VALUE"]:
                    print(f"Detected large buy order: {tx.value} Wei")
                    return True
    except Exception as e:
        print(f"Error decoding transaction {tx.hash.hex()}: {e}")
    return False

if __name__ == "__main__":
    monitor_mempool()
