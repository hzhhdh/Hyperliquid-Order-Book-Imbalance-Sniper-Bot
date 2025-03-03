// Example using SPL Token Multisig on Solana
import { PublicKey, Transaction } from '@solana/web3.js';

const multisig = new PublicKey("MULTISIG_WALLET_ADDRESS");

// Create a transaction requiring 3/5 signatures
const transaction = new Transaction().add(
    // Add rebalancing or withdrawal instructions
);

// Sign and send transaction
await multisig.signAndSend(transaction, [signer1, signer2, signer3]);
