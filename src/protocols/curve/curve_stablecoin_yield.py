from curve import CurvePool
import requests
import logging

logging.basicConfig(level=logging.INFO, filename='curve.log')

class CurveStablecoinYield:
    def __init__(self, pool_address):
        self.pool = CurvePool(pool_address)
        self.graph_api = "https://api.thegraph.com/subgraphs/name/curvefi/curve"

    def fetch_pool_yield(self):
        query = """
        {
            pools(where: {id: "%s"}) {
                virtualPrice
                dailyAPY
            }
        }
        """ % self.pool.address
        try:
            response = requests.post(self.graph_api, json={'query': query})
            return response.json()['data']['pools'][0]['dailyAPY']
        except Exception as e:
            logging.error(f"Error fetching yield: {e}")
            raise

    def optimize_yield(self, amount):
        apy = self.fetch_pool_yield()
        if apy > 3.0:
            self.pool.add_liquidity(amount)
            logging.info(f"Added {amount} to Curve pool, APY: {apy}%")
        else:
            logging.info(f"APY too low: {apy}%")

if __name__ == "__main__":
    yield_bot = CurveStablecoinYield("0x...")
    yield_bot.optimize_yield(1000)
