async def rebalance_portfolio():
    pools = await fetch_balancer_pools()
    weights = calculate_optimal_weights(pools)
    await adjust_pool_positions(weights)
