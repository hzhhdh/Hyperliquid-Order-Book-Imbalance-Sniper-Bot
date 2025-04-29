async def manage_lido_staking():
    await stake_eth(amount=1.0)
    steth_balance = await check_steth_balance()
    await deposit_steth_to_pool(steth_balance)
