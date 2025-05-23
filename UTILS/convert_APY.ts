export function calculateDailyYield(apy: number): number {
  return (apy / 100) / 365;
}
