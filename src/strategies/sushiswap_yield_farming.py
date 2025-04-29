async def farm_sushiswap_pool(pool_id: int):
    await stake_tokens(pool_id, amount)
    while True:
        rewards = await check_pending_rewards(pool_id)
        if rewards > min_threshold:
            await reinvest_rewards(rewards)
        await asyncio.sleep(60)
