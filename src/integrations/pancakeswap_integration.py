async def swap_pancakeswap(token_in: str, token_out: str, amount: float):
    router = get_pancakeswap_router_contract()
    tx = await router.functions.swapExactTokensForTokens(amount, token_in, token_out)
    return tx
