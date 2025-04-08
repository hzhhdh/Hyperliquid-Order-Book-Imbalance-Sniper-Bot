from dex_loader import dex_contract

def decode_tx_input(input_data):
    # This function uses the contract instance to decode the transaction data
    try:
        func_obj, params = dex_contract.decode_function_input(input_data)
        return func_obj, params
    except Exception as e:
        raise Exception(f"Decoding failed: {e}")
