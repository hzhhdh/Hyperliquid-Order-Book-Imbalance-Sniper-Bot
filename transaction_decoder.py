from dex_loader import dex_contract

def decode_tx_input(input_data):
    try:
        func_obj, params = dex_contract.decode_function_input(input_data)
        return func_obj, params
    except Exception as e:
        raise Exception(f"Decoding transaction input failed: {e}")

if __name__ == "__main__":
    sample_input = "0x"  # Replace with a sample transaction input for testing.
    print(decode_tx_input(sample_input))
