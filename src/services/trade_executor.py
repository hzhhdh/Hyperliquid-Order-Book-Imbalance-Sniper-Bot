from web3 import Web3

class TradeExecutor:
    """Executes trades either on-chain or via Flashbots."""
    def __init__(self, web3: Web3, flashbots: FlashbotsIntegration, gas_cap: int):
        self.web3 = web3
        self.flashbots = flashbots
        self.gas_cap = gas_cap

    def execute_trade(self, tx, use_flashbots=False):
        if use_flashbots and self.web3.eth.gas_price > self.gas_cap:
            return self.flashbots.send_bundle([tx], self.web3.eth.block_number + 1)
        return self.web3.eth.send_raw_transaction(tx.rawTransaction)
