class RugpullDetector:
    def __init__(self, client: BlockchainClient):
        self.client = client

    async def check_rugpull(self, contract_address: str) -> bool:
        liquidity = await self.client.get_pool_liquidity(contract_address)
        if liquidity < min_threshold:
            logger.warning(f"Rugpull detected for {contract_address}")
            return True
        return False
