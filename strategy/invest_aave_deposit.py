from web3 import Web3
from aave_web3_py import Aave

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_KEY"))
aave = Aave(w3, "0xLENDING_POOL_ADDRESS", "0xYOUR_PRIVATE_KEY")
tx_hash = aave.deposit(
    asset=STETH_ADDRESS,
    amount=w3.to_wei(1.0, 'ether'),
    onBehalfOf=aave.account.address,
    referralCode=0
)
print(f"Aave deposit tx: {tx_hash}")
