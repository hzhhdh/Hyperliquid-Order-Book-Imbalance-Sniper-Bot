export function getWalletStatus(): string {
  return window.ethereum?.isConnected() ? 'Connected' : 'Disconnected';
}
