from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_KEY'))

def place_dydx_order(side: str, amount: float):
    contract = w3.eth.contract(address='0x...', abi=ABI)
    tx = contract.functions.trade(
        asset='ETH',
        amount=Web3.to_wei(amount, 'ether'),
        side=side
    ).build_transaction({
        'gas': 500000,
        'gasPrice': w3.eth.gas_price
    })
    return tx
