class DataFetcher:
    def __init__(self, exchange):
        self.exchange = exchange

    def fetch_market_data(self, pairs):
        data = {}
        for pair in pairs:
            data[pair] = {}
            for exchange_id in self.exchange.cex:
                data[pair][exchange_id] = self.exchange.fetch_price(exchange_id, pair)
            for exchange_id in self.exchange.dex:
                data[pair][exchange_id] = self.exchange.fetch_price(exchange_id, pair)
        return data
