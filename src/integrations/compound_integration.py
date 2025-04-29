async def lend_compound(asset: str, amount: float):
    ctoken = get_ctoken_contract(asset)
    await ctoken.functions.mint(amount).call()
