export function estimateRewards(amount: number, apy: number, days: number): number {
  return amount * calculateDailyYield(apy) * days;
}
