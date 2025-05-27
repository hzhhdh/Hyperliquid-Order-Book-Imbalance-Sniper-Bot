from config import *
from sniper_bot import SniperBot

if __name__ == "__main__":
    bot = SniperBot(PRIVATE_KEY, API_URL, COINS, PRICE_RANGE, IMBALANCE_RATIO, MIN_NOTIONAL)
    bot.run()
