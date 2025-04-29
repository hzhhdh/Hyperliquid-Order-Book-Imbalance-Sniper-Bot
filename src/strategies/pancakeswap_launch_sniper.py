async def snipe_pancakeswap_launch():
    pair_events = await monitor_pancakeswap_factory()
    for pair in pair_events:
        if is_new_token(pair.token0, pair.token1):
            tx = await build_pancakeswap_swap(pair)
            await execute_transaction(tx)
