export async function signTransaction(wallet: ethers.Wallet, tx: ethers.Transaction): Promise<string> {
  try {
    const signedTx = await wallet.signTransaction(tx);
    logInfo(`Signed transaction: ${signedTx}`);
    return signedTx;
  } catch (error) {
    throw new Error(`Transaction signing failed: ${parseBlockchainError(error)}`);
  }
}
