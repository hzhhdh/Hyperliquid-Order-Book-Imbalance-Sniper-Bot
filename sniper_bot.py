class SniperBot:
    def __init__(self, private_key, api_url, coins, price_range, imbalance_ratio, min_notional):
        self.private_key = private_key
        self.api_url = api_url
        self.coins = coins
        self.price_range = price_range
        self.imbalance_ratio = imbalance_ratio
        self.min_notional = min_notional
        
        self.info = Info(api_url, skip_ws=False)
        self.exchange = Exchange(api_url, private_key)
        self.meta = self.info.meta()
        self.coin_to_asset = {coin: i for i, coin in enumerate(self.meta["universe"])}
        self.order_books = {coin: None for coin in coins}
        self.lock = Lock()
        
        for coin in coins:
            self.info.subscribe(L2BookSubscription(coin), self.order_book_callback(coin))

    def order_book_callback(self, coin):
        def callback(msg):
            with self.lock:
                self.order_books[coin] = msg
        return callback

    def run(self):
        while True:
            for coin in self.coins:
                with self.lock:
                    ob = self.order_books.get(coin)
                if ob is None:
                    continue
                
                current_price = float(ob["mid_price"])
                buy_volume = sum(float(bid["sz"]) for bid in ob["bids"] if current_price * (1 - self.price_range) <= float(bid["px"]) <= current_price * (1 + self.price_range))
                sell_volume = sum(float(ask["sz"]) for ask in ob["asks"] if current_price * (1 - self.price_range) <= float(ask["px"]) <= current_price * (1 + self.price_range))
                
                if buy_volume > sell_volume * self.imbalance_ratio:
                    self.place_order(coin, SIDES.BUY, current_price)
                elif sell_volume > buy_volume * self.imbalance_ratio:
                    self.place_order(coin, SIDES.SELL, current_price)
            time.sleep(5)

    def place_order(self, coin, side, current_price):
        asset = self.coin_to_asset[coin]
        size = self.min_notional / current_price
        order_request = OrderRequest(
            side=side,
            size=size,
            price=None,
            asset=asset,
            tif="GTC",
            reduce_only=False,
        )
        try:
            self.exchange.submit_order(order_request)
            print(f"Placed {side.name} order for {coin}: size {size}")
        except Exception as e:
            print(f"Error placing {side.name} order for {coin}: {e}")
