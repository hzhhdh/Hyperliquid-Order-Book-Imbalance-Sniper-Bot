import os
import json
import logging
from web3 import Web3, HTTPProvider
from eth_account import Account
from dotenv import load_dotenv

# Load environment variables from .env (for RPC URLs, API keys, etc.)
load_dotenv()

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


def create_wallet(predefined_params: dict) -> dict:
    """
    Creates a 'smart wallet' with preset risk controls and returns wallet information.
    The parameters could include default spending limit, fee tolerance, and preferred tokens.
    """
    logging.info("Creating smart wallet with parameters: %s", predefined_params)
    # Create a new Ethereum account using a cryptographically secure function.
    wallet = Account.create()
    
    wallet_config = {
        'address': wallet.address,
        'private_key': wallet.privateKey.hex(),  # In production, secure this value!
        'spending_limit': predefined_params.get("default_spending_limit", 1_000_000),
        'fee_tolerance': predefined_params.get("fee_tolerance", 0.005),
        'risk_parameters': predefined_params.get("risk_parameters", {"max_trade_size": 100_000}),
        'preferred_tokens': predefined_params.get("preferred_tokens", ["USDC", "ETH", "RAY"])
    }
    logging.info("Wallet created with public address: %s", wallet_config['address'])
    return wallet_config


def connect_to_blockchain():
    """
    Establishes a connection to the blockchain using a custom RPC endpoint securely stored in environment variables.
    """
    rpc_url = os.getenv("ETH_RPC_ENDPOINT")
    if not rpc_url:
        logging.error("RPC endpoint not set. Please define ETH_RPC_ENDPOINT in environment variables.")
        raise EnvironmentError("Missing ETH_RPC_ENDPOINT")
    
    web3 = Web3(HTTPProvider(rpc_url))
    if web3.isConnected():
        logging.info("Connected to Ethereum network via RPC endpoint.")
    else:
        logging.error("Failed to connect to Ethereum network.")
        raise ConnectionError("Blockchain connection failed")
    return web3


def sign_transaction(web3, tx: dict, private_key: str) -> dict:
    """
    Signs a transaction securely and logs the process.
    """
    try:
        logging.info("Signing transaction: %s", tx)
        signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
        logging.info("Transaction signed successfully.")
        return signed_tx
    except Exception as e:
        logging.error("Failed to sign transaction: %s", e)
        raise


def send_transaction(web3, signed_tx: dict) -> str:
    """
    Sends a signed transaction to the blockchain and returns its hash.
    """
    try:
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        logging.info("Transaction sent. Hash: %s", tx_hash.hex())
        return tx_hash.hex()
    except Exception as e:
        logging.error("Failed to send transaction: %s", e)
        raise


if __name__ == "__main__":
    # Example workflow to create a wallet, connect to blockchain, sign and send a transaction
    predefined_params = {
        "default_spending_limit": 1_000_000,
        "fee_tolerance": 0.005,
        "risk_parameters": {"max_trade_size": 100_000},
        "preferred_tokens": ["USDC", "ETH", "RAY"]
    }
    
    wallet = create_wallet(predefined_params)
    web3 = connect_to_blockchain()
    
    # Example transaction: sending a small value (0 ETH) from the newly created wallet (for demo)
    tx = {
        'nonce': web3.eth.get_transaction_count(wallet['address']),
        'to': wallet['address'],  # Self-transfer for demo purposes
        'value': 0,
        'gas': 21000,
        'gasPrice': web3.toWei('50', 'gwei')
    }
    
    signed_tx = sign_transaction(web3, tx, wallet['private_key'])
    tx_hash = send_transaction(web3, signed_tx)
    logging.info("Demo transaction completed. Tx Hash: %s", tx_hash)
