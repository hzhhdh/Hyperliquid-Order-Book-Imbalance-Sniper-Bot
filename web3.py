from web3 import AsyncWeb3, AsyncHTTPProvider
import asyncio

# RPC endpoint (Infura) and account setup
API_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
PRIVATE_KEY = "0xYOUR_PRIVATE_KEY"

def build_transaction(w3, to, value_ether):
    nonce = w3.eth.get_transaction_count(w3.eth.account.privateKeyToAccount(PRIVATE_KEY).address)
    tx = {
        'to': to,
        'value': w3.to_wei(value_ether, 'ether'),
        'gas': 21000,
        'maxFeePerGas': w3.to_wei('50', 'gwei'),
        'maxPriorityFeePerGas': w3.to_wei('2', 'gwei'),
        'nonce': nonce,
        'chainId': 1
    }
    return tx

async def send_eth():
    w3 = AsyncWeb3(AsyncHTTPProvider(API_URL))
    acct = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)
    tx = build_transaction(w3, '0xAbC123...DEF', 0.1)
    signed = acct.sign_transaction(tx)
    tx_hash = await w3.eth.send_raw_transaction(signed.rawTransaction)
    print(f"Transaction sent: {tx_hash.hex()}")

asyncio.run(send_eth())
