# Liquid stacking module via Lido (ETH -> stETH)
from web3 import Web3
from eth_abi import encode

def stake_eth(w3: Web3, amount: float, validator_key: str) -> str:
    lido_contract = w3.eth.contract(
        address="0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84",
        abi=lido_abi
    )
    
    tx = lido_contract.functions.submit(validator_key).build_transaction({
        'value': w3.to_wei(amount, 'ether'),
        'gas': 250000,
        'nonce': w3.eth.get_transaction_count(w3.eth.default_account),
    })
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=user_pk)
    return w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()

# A test using Ganache
def test_staking(ganache_provider):
    w3 = Web3(ganache_provider)
    tx_hash = stake_eth(w3, 1.0, "0x...")
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    assert receipt['status'] == 1
