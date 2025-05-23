export function generateTxId(): string {
  return `tx_${Date.now()}_${Math.random().toString(36).slice(2)}`;
}
