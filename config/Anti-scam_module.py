# Verifying the honeypot token
def is_honeypot(token_address: str, w3: Web3) -> bool:
    try:
        contract = w3.eth.contract(
            address=token_address,
            abi=ERC20_ABI
        )
        
        # Verification of saleability
        sell_tx = contract.functions.transfer(
            "0x000000000000000000000000000000000000dEaD", 
            1
        ).build_transaction({'from': user_address})
        
        # Transaction simulation
        try:
            w3.eth.call(sell_tx)
            return False
        except Exception as e:
            if "execution reverted" in str(e):
                return True
    except:
        return True
    
    return False
