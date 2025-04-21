from web3 import Web3
from chainlink_web3 import ChainlinkPriceFeed

class PriceFeedService:
    """Fetches latest token prices from Chainlink oracles."""
    def __init__(self, web3: Web3):
        self.chainlink = ChainlinkPriceFeed(web3)

    def get_price(self, feed_address: str) -> float:
        return self.chainlink.get_price(feed_address)
