class ArbitrageBot:
    def __init__(self):
        self.dex = UniswapClient()
        self.cex = BinanceClient()

    async def run(self):
        while True:
            dex_price = self.dex.get_price()
            cex_price = self.cex.get_price()
            if self.check_spread(dex_price, cex_price):
                self.execute_trade()
            await asyncio.sleep(5)
