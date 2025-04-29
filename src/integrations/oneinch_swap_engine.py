async def swap_oneinch(token_in: str, token_out: str, amount: float):
    swap_data = await fetch_oneinch_swap_data(token_in, token_out, amount)
    tx = await build_swap_tx(swap_data)
    return tx
