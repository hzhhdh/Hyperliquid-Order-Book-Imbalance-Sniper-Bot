from web3 import Web3
from config import CONFIG

def get_rpc_provider():
    network = CONFIG["SELECTED_NETWORK"]
    if network in CONFIG["CUSTOM_RPC_ENDPOINTS"] and CONFIG["CUSTOM_RPC_ENDPOINTS"][network]:
        rpc_url = CONFIG["CUSTOM_RPC_ENDPOINTS"][network]
    else:
        rpc_url = CONFIG["AVAILABLE_NETWORKS"].get(network)
    if not rpc_url:
        raise ValueError(f"No RPC endpoint found for network: {network}")
    print(f"Connecting to {network} using RPC endpoint: {rpc_url}")
    return Web3(Web3.HTTPProvider(rpc_url))

w3 = get_rpc_provider()
