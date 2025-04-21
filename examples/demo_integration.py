from web3 import Web3
from services.flashbots_integration import FlashbotsIntegration
from services.price_feed_service import PriceFeedService

if __name__ == "__main__":
    w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
    fb = FlashbotsIntegration("https://relay.flashbots.net", signer_key="KEY")
    pf = PriceFeedService(w3)
    price = pf.get_price("0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419")
    print(f"ETH/USD price: {price}")
