// Example: Proof of reserves using Merkle trees
const { MerkleTree } = require('merkletreejs');
const crypto = require('crypto');

// Generate Merkle tree for user balances
const leaves = userBalances.map(b => crypto.createHash('sha256').update(b).digest());
const tree = new MerkleTree(leaves, crypto.createHash('sha256'));

// Publish root hash on-chain
const rootHash = tree.getRoot().toString('hex');
console.log("Merkle Root Hash:", rootHash);
