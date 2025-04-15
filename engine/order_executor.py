import time
from config import CONFIG
from dex_loader import dex_contract
from network import w3
from gas_optimizer import get_premium_gas_price

def execute_preemptive_order():
    try:
        premium_gas_price = get_premium_gas_price()
        deadline = int(time.time()) + CONFIG["TRANSACTION_DEADLINE_OFFSET"]

        # Calculate minimum tokens expected using slippage tolerance.
        expected_tokens = get_expected_tokens(CONFIG["TRADE_AMOUNT"])
        min_tokens = int(expected_tokens * CONFIG["SLIPPAGE_TOLERANCE_FACTOR"])

        tx = dex_contract.functions.swapExactETHForTokens(
            min_tokens,
            [CONFIG["BUY_TOKEN_ADDRESS"], CONFIG["TARGET_TOKEN_ADDRESS"]],
            CONFIG["YOUR_ADDRESS"],
            deadline
        ).buildTransaction({
            'from': CONFIG["YOUR_ADDRESS"],
            'value': CONFIG["TRADE_AMOUNT"],
            'gas': CONFIG["GAS_LIMIT"],
            'gasPrice': premium_gas_price,
            'nonce': w3.eth.getTransactionCount(CONFIG["YOUR_ADDRESS"])
        })

        signed_tx = w3.eth.account.sign_transaction(tx, CONFIG["PRIVATE_KEY"])
        tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Preemptive buy order sent successfully. Tx hash: {tx_hash.hex()}")
    except Exception as e:
        print(f"Error during order execution: {e}")

def get_expected_tokens(amount):
    # Placeholder: In a live system, you would call a pricing function like getAmountsOut.
    # Here we simulate an expected amount.
    return 1000  # Replace with real-time computation

if __name__ == "__main__":
    execute_preemptive_order()
