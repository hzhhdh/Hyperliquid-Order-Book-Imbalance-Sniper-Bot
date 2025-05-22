import logging
import random
from typing import Dict, List, Optional
from web3 import Web3
from web3.types import TxParams
from eth_account.signers.local import LocalAccount
from .utils import load_abi, calculate_slippage

logger = logging.getLogger(__name__)

class PancakeSwapDcaStrategy:
    """DCA strategy for PancakeSwap v2 with randomized gas for MEV protection."""
    
    def __init__(self, w3: Web3, config: Dict, account: LocalAccount):
        self.w3 = w3
        self.config = config
        self.account = account
        self.router_address = Web3.toChecksumAddress("0x10ED43C718714eb63d5aA57B78B54704E256024E")
        self.router_abi = load_abi("pancakeswap_router_abi.json")
        self.router = self.w3.eth.contract(address=self.router_address, abi=self.router_abi)
        self.slippage = config.get("slippage", 0.3) / 100
        self.gas_multiplier = config.get("gas_multiplier", 1.5)

    async def execute_dca(self, path: List[str], amount_in: int) -> Optional[str]:
        """Execute a DCA trade on PancakeSwap v2."""
        try:
            logger.info(f"Preparing DCA trade on PancakeSwap: {amount_in} {path[0]} -> {path[-1]}")
            
            # Calculate minimum output with slippage
            amount_out_min = calculate_slippage(amount_in, self.slippage)
            
            # Build transaction with randomized gas
            tx_params: TxParams = {
                "from": self.account.address,
                "nonce": self.w3.eth.get_transaction_count(self.account.address),
                "gasPrice": int(self.w3.eth.gas_price * random.uniform(self.gas_multiplier, self.gas_multiplier * 1.5)),
                "chainId": self.config["chain_id"],
            }
            
            # PancakeSwap swapExactTokensForTokens call
            swap_call = self.router.functions.swapExactTokensForTokens(
                amountIn=amount_in,
                amountOutMin=amount_out_min,
                path=[Web3.toChecksumAddress(token) for token in path],
                to=self.account.address,
                deadline=int((self.w3.eth.get_block("latest")["timestamp"]) + 1800)
            ).buildTransaction(tx_params)
            
            # Sign and send transaction
            signed_tx = self.w3.eth.account.sign_transaction(swap_call, self.account.key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()
            
            logger.info(f"PancakeSwap DCA trade submitted: {tx_hash}")
            return tx_hash
        
        except Exception as e:
            logger.error(f"PancakeSwap DCA trade failed: {str(e)}")
            return None
