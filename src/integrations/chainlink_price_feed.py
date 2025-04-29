class ChainlinkPriceFeed:
    def __init__(self, client: BlockchainClient):
        self.client = client
        self.price_feed_address = "0x...  # Chainlink ETH/USD feed
        self.price_feed_abi = [...]  # Chainlink AggregatorV3 ABI

    async def get_price(self, token_address: str) -> float:
        w3 = self.client.web3_clients["ethereum"]
        price_feed = w3.eth.contract(address=self.price_feed_address, abi=self.price_feed_abi)
        return price_feed.functions.latestRoundData().call()[1] / 1e8
