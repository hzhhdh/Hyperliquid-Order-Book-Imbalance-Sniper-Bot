# Continuing from invest_aave_deposit.py context
tx_hash = aave.borrow(
    asset=ETH_ADDRESS,
    amount=w3.to_wei(0.5, 'ether'),
    interestRateMode=2,  # variable rate
    onBehalfOf=aave.account.address,
    referralCode=0
)
print(f"Aave borrow tx: {tx_hash}")
