import asyncio
from web3 import AsyncWeb3, AsyncHTTPProvider

async def watch_mempool():
    w3 = AsyncWeb3(AsyncHTTPProvider("https://mainnet.infura.io/v3/KEY"))
    async for tx in w3.txpool.contentious_transactions():
        print(tx)

asyncio.run(watch_mempool())
