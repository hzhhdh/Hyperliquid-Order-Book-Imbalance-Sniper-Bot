async def stake_lido(amount: float):
    lido = get_lido_staking_contract()
    await lido.functions.submit(amount).call()
