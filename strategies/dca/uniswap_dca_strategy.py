import logging
from typing import Dict, Optional
from web3 import Web3
from web3.types import TxParams
from eth_account.signers.local import LocalAccount
from .utils import load_abi, calculate_slippage, get_gas_estimate

logger = logging.getLogger(__name__)

class UniswapDcaStrategy:
    """DCA strategy for Uniswap v3 with MEV protection and slippage control."""
    
    def __init__(self, w3: Web3, config: Dict, account: LocalAccount):
        self.w3 = w3
        self.config = config
        self.account = account
        self.router_address = Web3.toChecksumAddress("0xE592427A0AEce92De3Edee1F18E0157C05861564")
        self.router_abi = load_abi("uniswap_v3_router_abi.json")
        self.router = self.w3.eth.contract(address=self.router_address, abi=self.router_abi)
        self.slippage = config.get("slippage", 0.3) / 100  # Default 0.3%
        self.flashbots_enabled = config.get("flashbots", True)

    async def execute_dca(self, token_in: str, token_out: str, amount_in: int, fee: int = 3000) -> Optional[str]:
        """Execute a DCA trade on Uniswap v3 with MEV protection."""
        try:
            logger.info(f"Preparing DCA trade: {amount_in} {token_in} -> {token_out}")
            
            # Calculate slippage and minimum output
            amount_out_min = calculate_slippage(amount_in, self.slippage)
            
            # Build transaction
            tx_params: TxParams = {
                "from": self.account.address,
                "nonce": self.w3.eth.get_transaction_count(self.account.address),
                "gas": get_gas_estimate(self.w3, self.router_address),
                "chainId": self.config["chain_id"],
            }
            
            # Uniswap v3 exactInputSingle call
            swap_call = self.router.functions.exactInputSingle(
                tokenIn=Web3.toChecksumAddress(token_in),
                tokenOut=Web3.toChecksumAddress(token_out),
                fee=fee,
                recipient=self.account.address,
                deadline=int((self.w3.eth.get_block("latest")["timestamp"]) + 1800),
                amountIn=amount_in,
                amountOutMinimum=amount_out_min,
                sqrtPriceLimitX96=0
            ).buildTransaction(tx_params)
            
            # Apply MEV protection via Flashbots
            if self.flashbots_enabled:
                bundle = self._prepare_flashbots_bundle(swap_call)
                tx_hash = await self._submit_flashbots_bundle(bundle)
            else:
                signed_tx = self.w3.eth.account.sign_transaction(swap_call, self.account.key)
                tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()
            
            logger.info(f"DCA trade submitted: {tx_hash}")
            return tx_hash
        
        except Exception as e:
            logger.error(f"DCA trade failed: {str(e)}")
            return None

    def _prepare_flashbots_bundle(self, tx: Dict) -> List[Dict]:
        """Prepare a Flashbots bundle for MEV protection."""
        # Simulated Flashbots bundle preparation (implementation omitted for brevity)
        return [{"signed_transaction": tx}]
