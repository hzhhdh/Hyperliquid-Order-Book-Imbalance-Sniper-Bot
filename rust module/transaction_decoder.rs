pub mod transaction_decoder {
    use ethers::abi::Abi;
    use ethers::contract::Contract;
    use ethers::types::Bytes;
    use std::fs::File;
    use std::io::Read;

    pub fn load_abi_from_file(filename: &str) -> Abi {
        let mut file = File::open(filename).expect(&format!("ABI file {} not found", filename));
        let mut contents = String::new();
        file.read_to_string(&mut contents).expect("Failed to read ABI file");
        serde_json::from_str::<Abi>(&contents).expect("Failed to parse ABI")
    }

    pub fn decode_tx_input(contract: &Contract<ethers::providers::Provider<ethers::providers::Http>>, input: Bytes)
        -> Result<(ethers::abi::Function, ethers::abi::Token), Box<dyn std::error::Error>> {
        // Use contract.decode_function_data provided by ethers-rs
        // Note: This is a simplified interface; in production, handle multiple parameters properly.
        let decoded = contract.decode_input(&input)?;
        Ok(decoded)
    }
}
