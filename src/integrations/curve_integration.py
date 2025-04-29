async def add_curve_liquidity(pool_address: str, amounts: list):
    curve_pool = get_curve_pool_contract(pool_address)
    await curve_pool.functions.add_liquidity(amounts).call()
