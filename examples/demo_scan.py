from web3 import Web3
from services.arbitrage_scanner import ArbitrageScanner

if __name__ == "__main__":
    w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))
    arb = ArbitrageScanner(w3, ["UniswapV3", "Binance"], min_profit=100.0)
    print(arb.scan())
