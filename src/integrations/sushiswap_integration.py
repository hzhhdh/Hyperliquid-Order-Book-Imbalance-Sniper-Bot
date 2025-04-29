async def stake_sushiswap(pool_id: int, amount: float):
    masterchef = get_sushiswap_masterchef_contract()
    await masterchef.functions.deposit(pool_id, amount).call()
