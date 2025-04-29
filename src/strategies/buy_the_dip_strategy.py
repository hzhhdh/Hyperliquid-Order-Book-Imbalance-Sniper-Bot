import asyncio
from ..core.blockchain_client import BlockchainClient
from ..integrations.chainlink_price_feed import ChainlinkPriceFeed
from ..utils.logger import logger

class BuyTheDipStrategy:
    def __init__(self, client: BlockchainClient, chainlink: ChainlinkPriceFeed):
        self.client = client
        self.chainlink = chainlink
        self.dip_threshold = 0.1  # 10% drop

    async def monitor_dip(self, token_address: str):
        try:
            while True:
                price = await self.chainlink.get_price(token_address)
                historical_price = await self.chainlink.get_historical_price(token_address, hours=1)
                if (historical_price - price) / historical_price > self.dip_threshold:
                    tx = await self.client.build_swap_tx(token_address, amount=0.1)
                    signed_tx = await self.client.wallet_manager.sign_transaction("ethereum", tx)
                    tx_hash = await self.client.web3_clients["ethereum"].eth.send_raw_transaction(signed_tx.rawTransaction)
                    logger.info(f"Bought dip for {token_address}: {tx_hash.hex()}")
                await asyncio.sleep(60)
        except Exception as e:
            logger.error(f"Error in buy-the-dip strategy: {e}")

async def main():
    client = BlockchainClient()
    chainlink = ChainlinkPriceFeed(client)
    strategy = BuyTheDipStrategy(client, chainlink)
    await strategy.monitor_dip("0x...")  # Token address

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    asyncio.run(main())
