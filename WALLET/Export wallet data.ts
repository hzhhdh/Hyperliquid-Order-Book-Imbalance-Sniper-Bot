export function exportWalletData(address: string): string {
  return JSON.stringify({ address, timestamp: Date.now() });
}
