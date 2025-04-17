from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_KEY"))
acct = w3.eth.account.from_key("0xYOUR_PRIVATE_KEY")
router = w3.eth.contract(address="0xE592427A0AEce92De3Edee1F18E0157C05861564", abi=UNISWAP_V3_ROUTER)

params = {
    'tokenIn': WETH_ADDRESS,
    'tokenOut': USDC_ADDRESS,
    'fee': 3000,
    'recipient': acct.address,
    'deadline': w3.eth.get_block('latest')['timestamp'] + 300,
    'amountIn': w3.to_wei(0.5, 'ether'),
    'amountOutMinimum': 0,
    'sqrtPriceLimitX96': 0
}
tx = router.functions.exactInputSingle(params).build_transaction({
    'from': acct.address, 'nonce': w3.eth.get_transaction_count(acct.address)
})
signed = acct.sign_transaction(tx)
print("Uniswap V3 sell tx:", w3.eth.send_raw_transaction(signed.rawTransaction).hex())
