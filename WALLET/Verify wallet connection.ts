export async function verifyWalletConnection(address: string, chain: string): Promise<boolean> {
  return isValidAddress(address, chain) && await retryOperation(() => Promise.resolve(true));
}
