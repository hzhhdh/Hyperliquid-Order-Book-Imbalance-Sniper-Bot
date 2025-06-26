from solana.rpc.async_api import AsyncClient
from raydium_sdk import AMM, OpenBook

async def raydium_swap(client: AsyncClient, wallet: dict, token_address: str, amount: float, side: str):
    """Execute a swap on Raydium."""
    amm = AMM(token_address)
    try:
        if side == "buy":
            tx = amm.market_buy(wallet['public_key'], wallet['private_key'], amount, slippage=0.01)
        else:
            tx = amm.market_sell(wallet['public_key'], wallet['private_key'], amount, slippage=0.01)
        result = await client.send_transaction(tx)
        print(f"Raydium {side} executed: {result}")
    except Exception as e:
        print(f"Raydium swap error: {str(e)}")
