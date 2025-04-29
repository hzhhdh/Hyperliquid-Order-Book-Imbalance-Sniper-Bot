async def trade_enginlayer(token: str, amount: float):
    dex = get_enginlayer_dex_contract()
    await dex.functions.swap(token, amount).call()
