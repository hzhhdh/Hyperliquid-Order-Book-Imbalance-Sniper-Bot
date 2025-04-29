import asyncio
from web3 import Web3
from solana.rpc.async_api import AsyncClient
from .config_manager import ConfigManager

class BlockchainClient:
    def __init__(self):
        self.config = ConfigManager()
        self.web3_clients = {}
        self.solana_client = None

    async def initialize_evm_client(self, chain_id: str, rpc_url: str):
        try:
            self.web3_clients[chain_id] = Web3(Web3.WebsocketProvider(rpc_url))
            if not self.web3_clients[chain_id].is_connected():
                raise ConnectionError(f"Failed to connect to {chain_id}")
        except Exception as e:
            logger.error(f"Error initializing EVM client for {chain_id}: {e}")
            raise

    async def initialize_solana_client(self, rpc_url: str):
        try:
            self.solana_client = AsyncClient(rpc_url)
            if not await self.solana_client.is_connected():
                raise ConnectionError("Failed to connect to Solana")
        except Exception as e:
            logger.error(f"Error initializing Solana client: {e}")
            raise

    async def get_block_events(self, chain_id: str, contract_address: str):
        # Subscribe to contract events (e.g., new pair creation)
        pass
