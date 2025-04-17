from web3 import Web3

# Setup
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_KEY"))
private_key = "0xYOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)
router = w3.eth.contract(address="0xROUTER_ADDRESS", abi=ROUTER_ABI)

# Build and send approve tx
nonce = w3.eth.get_transaction_count(account.address)
tx = router.functions.approve(
    "0xTOKEN_ADDRESS",
    w3.to_wei(1_000_000, 'ether')
).build_transaction({
    'from': account.address,
    'nonce': nonce,
    'gas': 100_000,
    'maxFeePerGas': w3.to_wei('50', 'gwei'),
    'maxPriorityFeePerGas': w3.to_wei('2', 'gwei'),
})
signed = account.sign_transaction(tx)
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
print(f"Approve sent: {tx_hash.hex()}")
