from chainlink_web3 import ChainlinkPriceFeed

class ChainlinkIntegration:
    """Simplifies Chainlink oracle queries."""
    def __init__(self, web3):
        self.feed = ChainlinkPriceFeed(web3)

    def fetch(self, address):
        return self.feed.get_price(address)
