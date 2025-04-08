import json
from config import CONFIG
from network import w3

def load_dex_contract():
    dex_name = CONFIG["SELECTED_DEX"]
    dex_info = CONFIG["AVAILABLE_DEXES"].get(dex_name)
    if not dex_info:
        raise ValueError(f"DEX {dex_name} not available in configuration.")
    router_address = dex_info["router_address"]
    abi_file = dex_info["abi_file"]
    try:
        with open(abi_file, "r") as f:
            abi = json.load(f)
    except Exception as e:
        raise Exception(f"Error loading ABI file '{abi_file}': {e}")
    contract = w3.eth.contract(address=router_address, abi=abi)
    print(f"{dex_name} contract loaded at address {router_address}")
    return contract

dex_contract = load_dex_contract()
