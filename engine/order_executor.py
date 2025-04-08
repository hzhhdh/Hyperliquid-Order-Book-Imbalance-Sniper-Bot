import time
from config import CONFIG
from dex_loader import dex_contract
from network import w3

def execute_preemptive_order():
    try:
        current_gas_price = w3.eth.gasPrice
        premium_gas_price = int(current_gas_price * CONFIG["GAS_PREMIUM_MULTIPLIER"])
        deadline = int(time.time()) + CONFIG["TRANSACTION_DEADLINE_OFFSET"]

        # Calculate expected minimum tokens based on slippage tolerance. This is typically dynamic.
        # Here we assume a placeholder function get_expected_tokens() exists.
        expected_tokens = get_expected_tokens(CONFIG["TRADE_AMOUNT"])
        min_tokens = int(expected_tokens * CONFIG["SLIPPAGE_TOLERANCE_FACTOR"])

        tx = dex_contract.functions.swapExactETHForTokens(
            min_tokens,
            [CONFIG["BUY_TOKEN_ADDRESS"], CONFIG["TARGET_TOKEN_ADDRESS"]],
            CONFIG.get("YOUR_ADDRESS", "0xYourWalletAddress"),  # Replace with actual wallet address management
            deadline
        ).buildTransaction({
            'from': CONFIG.get("YOUR_ADDRESS", "0xYourWalletAddress"),
            'value': CONFIG["TRADE_AMOUNT"],
            'gas': CONFIG["GAS_LIMIT"],
            'gasPrice': premium_gas_price,
            'nonce': w3.eth.getTransactionCount(CONFIG.get("YOUR_ADDRESS", "0xYourWalletAddress"))
        })
        
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=CONFIG.get("PRIVATE_KEY", "YOUR_PRIVATE_KEY"))
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Preemptive buy order sent with tx hash: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error executing preemptive order: {e}")

def get_expected_tokens(amount):
    # Placeholder function: In production, query the DEX for expected output (using getAmountsOut, for example)
    return 1000  # Replace with dynamic calculation based on pool reserves
