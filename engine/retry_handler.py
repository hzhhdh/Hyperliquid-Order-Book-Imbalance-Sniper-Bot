import time
from config import CONFIG

def retry_on_failure(func):
    def wrapper(*args, **kwargs):
        attempts = 0
        while attempts < CONFIG["MAX_RETRY_ATTEMPTS"]:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                attempts += 1
                print(f"Attempt {attempts} failed: {e}. Retrying...")
                time.sleep(1)  # Delay between retries, adjust if needed
        raise Exception(f"Operation failed after {CONFIG['MAX_RETRY_ATTEMPTS']} attempts.")
    return wrapper

# Example usage in order execution functions (can wrap execute_preemptive_order)
