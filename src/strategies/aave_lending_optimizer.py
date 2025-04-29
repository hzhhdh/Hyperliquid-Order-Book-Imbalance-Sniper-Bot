import asyncio
from ..core.blockchain_client import BlockchainClient
from ..integrations.aave_integration import AaveIntegration
from ..utils.logger import logger

class AaveLendingOptimizer:
    def __init__(self, client: BlockchainClient, aave: AaveIntegration):
        self.client = client
        self.aave = aave
        self.min_rate_threshold = 0.05  # 5% APY

    async def optimize_lending(self):
        try:
            while True:
                markets = await self.aave.get_lending_markets()
                best_market = max(markets, key=lambda x: x["apy"])
                if best_market["apy"] > self.min_rate_threshold:
                    tx = await self.aave.build_deposit_tx(best_market["asset"], amount=1.0)
                    signed_tx = await self.client.wallet_manager.sign_transaction("ethereum", tx)
                    tx_hash = await self.client.web3_clients["ethereum"].eth.send_raw_transaction(signed_tx.rawTransaction)
                    logger.info(f"Deposited to Aave market {best_market['asset']}: {tx_hash.hex()}")
                await asyncio.sleep(60)
        except Exception as e:
            logger.error(f"Error optimizing Aave lending: {e}")

async def main():
    client = BlockchainClient()
    aave = AaveIntegration(client)
    optimizer = AaveLendingOptimizer(client, aave)
    await optimizer.optimize_lending()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    asyncio.run(main())
