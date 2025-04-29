async def join_balancer_pool(pool_id: str, assets: list):
    vault = get_balancer_vault_contract()
    await vault.functions.joinPool(pool_id, assets).call()
