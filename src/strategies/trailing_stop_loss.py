async def trailing_stop_loss(token_address: str, trailing_percent: float):
    peak_price = await get_peak_price(token_address)
    current_price = await get_current_price(token_address)
    if current_price < peak_price * (1 - trailing_percent):
        await sell_token(token_address, amount=position_size)
