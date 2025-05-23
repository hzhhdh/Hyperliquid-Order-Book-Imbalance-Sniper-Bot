export function updateStakeMetrics(stakes: { [key: string]: number }): void {
  logInfo(`Updated stakes: ${JSON.stringify(stakes)}`);
}
