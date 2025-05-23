export async function importWallet(data: string): Promise<string> {
  try {
    const { address } = JSON.parse(data);
    if (!isValidAddress(address, 'eth')) throw new Error('Invalid address');
    return address;
  } catch (error) {
    throw new Error(`Wallet import failed: ${error.message}`);
  }
}
