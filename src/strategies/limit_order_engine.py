async def place_limit_order(token_address: str, price_target: float, amount: float):
    while True:
        current_price = await get_current_price(token_address)
        if abs(current_price - price_target) < 0.01:
            await execute_order(token_address, amount)
        await asyncio.sleep(10)
