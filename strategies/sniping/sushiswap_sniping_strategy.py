import logging
from typing import Dict, List, Optional
from web3 import Web3
from web3.types import TxParams
from eth_account.signers.local import LocalAccount
from .utils import load_abi, validate_contract, calculate_slippage

logger = logging.getLogger(__name__)

class SushiSwapSnipingStrategy:
    """Sniping strategy for SushiSwap with high-speed transactions and contract validation."""
    
    def __init__(self, w3: Web3, config: Dict, account: LocalAccount):
        self.w3 = w3
        self.config = config
        self.account = account
        self.router_address = Web3.toChecksumAddress("0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F")
        self.router_abi = load_abi("sushiswap_router_abi.json")
        self.router = self.w3.eth.contract(address=self.router_address, abi=self.router_abi)
        self.slippage = config.get("slippage", 0.5) / 100
        self.gas_multiplier = config.get("gas_multiplier", 2.0)

    async def execute_snipe(self, path: List[str], amount_in: int) -> Optional[str]:
        """Execute a high-speed snipe on SushiSwap."""
        try:
            logger.info(f"Preparing snipe: {amount_in} {path[0]} -> {path[-1]}")
            
            # Validate token contract
            if not await validate_contract(self.w3, path[-1]):
                logger.error("Invalid token contract detected")
                return None
            
            # Calculate slippage
            amount_out_min = calculate_slippage(amount_in, self.slippage)
            
            # Build high-speed transaction
            tx_params: TxParams = {
                "from": self.account.address,
                "nonce": self.w3.eth.get_transaction_count(self.account.address),
                "gasPrice": int(self.w3.eth.gas_price * self.gas_multiplier),
                "chainId": self.config["chain_id"],
            }
            
            # SushiSwap swapExactTokensForTokens call
            swap_call = self.router.functions.swapExactTokensForTokens(
                amountIn=amount_in,
                amountOutMin=amount_out_min,
                path=[Web3.toChecksumAddress(token) for token in path],
                to=self.account.address,
                deadline=int((self.w3.eth.get_block("latest")["timestamp"]) + 600)
            ).buildTransaction(tx_params)
            
            # Sign and send transaction
            signed_tx = self.w3.eth.account.sign_transaction(swap_call, self.account.key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()
            
            logger.info(f"SushiSwap snipe submitted: {tx_hash}")
            return tx_hash
        
        except Exception as e:
            logger.error(f"SushiSwap snipe failed: {str(e)}")
            return None
