async def manage_curve_liquidity(pool_address: str):
    pool_stats = await fetch_curve_pool_stats(pool_address)
    if pool_stats["imbalance"] > threshold:
        await rebalance_liquidity(pool_address)
    else:
        await add_liquidity(pool_address, amount)
