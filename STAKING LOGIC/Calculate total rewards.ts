export function calculateTotalRewards(stakes: { [key: string]: number }, apys: { [key: string]: number }): number {
  return Object.keys(stakes).reduce((sum, chain) => sum + stakes[chain] * calculateDailyYield(apys[chain]) * 30, 0);
}
