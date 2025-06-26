import requests
from src.utils.config import load_config

async def fetch_pumpfun_pools(min_liquidity: float) -> list:
    """Fetch new Pump.fun pools via Bitquery API."""
    config = load_config()
    query = """
    query {
        solana {
            dexTrades(where: {protocol: {is: "Pump.fun"}}) {
                token { address, holders }
                liquidityUSD
            }
        }
    }
    """
    response = requests.post("https://graphql.bitquery.io", json={"query": query}, headers={"X-API-KEY": config['bitquery_api_key']})
    pools = response.json()['data']['solana']['dexTrades']
    return [p for p in pools if p['liquidityUSD'] >= min_liquidity]
