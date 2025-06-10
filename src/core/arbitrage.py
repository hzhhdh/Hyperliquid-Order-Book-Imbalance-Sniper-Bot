from .exchange import Exchange

class Arbitrage:
    def __init__(self, exchange: Exchange, params: dict):
        self.exchange = exchange
        self.min_spread = params.get('min_spread', 0.5)
        self.max_gas_fee = params.get('max_gas_fee', 10.0)

    def find_opportunities(self, pairs):
        opportunities = []
        for pair in pairs:
            for cex_id in self.exchange.cex:
                for dex_id in self.exchange.dex:
                    cex_price = self.exchange.fetch_price(cex_id, pair)
                    dex_price = self.exchange.fetch_price(dex_id, pair)
                    spread = ((cex_price - dex_price) / dex_price) * 100
                    if spread >= self.min_spread:
                        opportunities.append({
                            'pair': pair,
                            'cex': cex_id,
                            'dex': dex_id,
                            'spread': spread,
                            'profit': (cex_price - dex_price) * 1.0  # Per unit
                        })
        return opportunities

    def execute_simple_arbitrage(self, opportunity, capital):
        # Placeholder for trade execution
        return {'profit': opportunity['profit'] * (capital / 1000)}
