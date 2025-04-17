from web3 import Web3
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/KEY"))
def check_peg():
    price = get_curve_price()
    if abs(price - 1.0) > 0.005:
        execute_trade()
