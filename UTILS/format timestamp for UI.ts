export function formatTimestamp(timestamp: number): string {
  return new Date(timestamp).toLocaleString('en-US', { timeZone: 'UTC' });
}
