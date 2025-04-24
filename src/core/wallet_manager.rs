use rand::Rng;
use ethers::signers::{LocalWallet, MnemonicBuilder};
use std::collections::HashMap;

pub struct InstitutionalWallet {
    pub wallets: HashMap<String, LocalWallet>,
    pub risk_limits: HashMap<String, u64>,
}

impl InstitutionalWallet {
    pub fn generate_batch(seed: &str, count: u16) -> Result<Self, String> {
        let mut wallets = HashMap::new();
        let mnemonic = MnemonicBuilder::<English>::default()
            .phrase(seed)
            .build()?;
        
        for i in 0..count {
            let wallet = mnemonic.derive(i as u32)?;
            wallets.insert(format!("wallet_{}", i), wallet);
        }
        
        Ok(InstitutionalWallet { wallets, risk_limits: HashMap::new() })
    }
}
