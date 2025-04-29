class AaveIntegration:
    def __init__(self, client: BlockchainClient):
        self.client = client
        self.lending_pool_address = "0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9"
        self.lending_pool_abi = [...]  # Aave LendingPool ABI

    async def build_deposit_tx(self, asset: str, amount: float) -> dict:
        w3 = self.client.web3_clients["ethereum"]
        lending_pool = w3.eth.contract(address=self.lending_pool_address, abi=self.lending_pool_abi)
        return lending_pool.functions.deposit(asset, amount, w3.eth.default_account, 0).build_transaction()
