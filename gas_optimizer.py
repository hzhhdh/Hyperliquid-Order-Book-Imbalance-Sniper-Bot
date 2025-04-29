async def optimize_gas(chain_id: str, tx: dict) -> dict:
    gas_price = await fetch_gas_price_from_api(chain_id)
    tx['gasPrice'] = min(gas_price * 1.2, max_gas_price)
    return tx
