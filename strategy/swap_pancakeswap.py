from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
acct = w3.eth.account.from_key("0xYOUR_PRIVATE_KEY")
router = w3.eth.contract(address="0x10ED43C718714eb63d5aA57B78B54704E256024E", abi=PANCAKESWAP_ROUTER)

# Quote and swap
amount_in = w3.to_wei(0.5, 'ether')
path = [w3.toChecksumAddress("0x...WBNB"), w3.toChecksumAddress("0x...BUSD")]
out = router.functions.getAmountsOut(amount_in, path).call()
print("Expect ~", w3.from_wei(out[-1], 'ether'), "BUSD")
tx = router.functions.swapExactETHForTokens(
    0, path, acct.address, w3.eth.get_block('latest')['timestamp']+300
).build_transaction({
    'from': acct.address,
    'value': amount_in,
    'nonce': w3.eth.get_transaction_count(acct.address)
})
signed = acct.sign_transaction(tx)
print("PancakeSwap tx:", w3.eth.send_raw_transaction(signed.rawTransaction).hex())
