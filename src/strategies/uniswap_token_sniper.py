import asyncio
from web3 import Web3
from ..core.blockchain_client import BlockchainClient
from ..integrations.uniswap_v3_integration import UniswapV3Integration
from ..utils.logger import logger

class UniswapTokenSniper:
    def __init__(self, client: BlockchainClient, uniswap: UniswapV3Integration):
        self.client = client
        self.uniswap = uniswap
        self.max_slippage = 0.05  # 5%

    async def monitor_new_pairs(self):
        try:
            w3 = self.client.web3_clients["ethereum"]
            factory = w3.eth.contract(address=self.uniswap.factory_address, abi=self.uniswap.factory_abi)
            while True:
                event_filter = factory.events.PairCreated.create_filter(fromBlock="latest")
                events = await event_filter.get_new_entries()
                for event in events:
                    await self.snipe_token(event.args.token0, event.args.token1)
                await asyncio.sleep(1.0 / 60)  # 60 FPS
        except Exception as e:
            logger.error(f"Error monitoring Uniswap pairs: {e}")

    async def snipe_token(self, token0: str, token1: str):
        try:
            pair_address = await self.uniswap.get_pair_address(token0, token1)
            price = await self.uniswap.get_pair_price(pair_address)
            if price < self.max_slippage:
                tx = await self.uniswap.build_swap_tx(token0, token1, amount=0.1)
                signed_tx = await self.client.wallet_manager.sign_transaction("ethereum", tx)
                tx_hash = await self.client.web3_clients["ethereum"].eth.send_raw_transaction(signed_tx.rawTransaction)
                logger.info(f"Sniped token pair {token0}/{token1}: {tx_hash.hex()}")
        except Exception as e:
            logger.error(f"Error sniping token: {e}")

async def main():
    client = BlockchainClient()
    uniswap = UniswapV3Integration(client)
    sniper = UniswapTokenSniper(client, uniswap)
    await sniper.monitor_new_pairs()

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    asyncio.run(main())
