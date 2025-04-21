from web3 import Web3, HTTPProvider
from flashbots import flashbot

class FlashbotsIntegration:
    """Submits transaction bundles via Flashbots Protect RPC."""
    def __init__(self, rpc_url: str, signer_key: str):
        self.w3 = Web3(HTTPProvider(rpc_url))
        flashbot(self.w3, signer_key)

    def send_bundle(self, signed_txs: list, target_block: int):
        return self.w3.flashbots.send_bundle(signed_txs, target_block)
