// ECDSA signature verification using `k256` library
use k256::{ecdsa::{Signature, VerifyingKey}, EncodedPoint};

pub fn verify_tx(signature: &[u8], public_key: &[u8], message: &[u8]) -> bool {
    let verifying_key = match VerifyingKey::from_encoded_point(
        &EncodedPoint::from_bytes(public_key).unwrap()
    ) {
        Ok(key) => key,
        Err(_) => return false,
    };
    
    let signature = match Signature::from_bytes(signature) {
        Ok(sig) => sig,
        Err(_) => return false,
    };
    
    verifying_key.verify(message, &signature).is_ok()
}

#[test]
fn test_signature_verification() {
    let message = b"Chimera DeFi Transaction";
    let (private_key, public_key) = generate_test_keys(); // Тестовые ключи
    let signature = sign_message(private_key, message);
    
    assert!(verify_tx(&signature, &public_key, message));
}
