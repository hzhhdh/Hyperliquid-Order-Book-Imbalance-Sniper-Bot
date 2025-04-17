from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_KEY"))
account = w3.eth.account.from_key("0xYOUR_PRIVATE_KEY")
curve = w3.eth.contract(address="0xCURVE_POOL", abi=CURVE_ABI)

# Quote and swap
amount_in = w3.to_wei(1.0, 'ether')
out = curve.functions.get_dy(1, 0, amount_in).call()  # index 1→0
print(f"Expect ~{w3.from_wei(out, 'ether')} ETH")  
tx = curve.functions.exchange(1, 0, amount_in, 0).build_transaction({
    'from': account.address, 'nonce': w3.eth.get_transaction_count(account.address)
})
signed = account.sign_transaction(tx)
print("Swap tx:", w3.eth.send_raw_transaction(signed.rawTransaction).hex())
