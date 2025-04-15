import json
from config import CONFIG

def load_config(filename="config.json"):
    try:
        with open(filename, "r") as f:
            user_config = json.load(f)
        CONFIG.update(user_config)
        print("Configuration successfully loaded from", filename)
    except Exception as e:
        print("Using default configuration due to error:", e)
    return CONFIG

def update_config(key, value):
    CONFIG[key] = value
    print(f"Config parameter {key} updated to {value}.")

if __name__ == "__main__":
    load_config()
