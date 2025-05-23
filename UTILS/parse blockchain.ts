export function parseBlockchainError(error: any): string {
  return error?.reason || error?.message || 'Unknown blockchain error';
}
