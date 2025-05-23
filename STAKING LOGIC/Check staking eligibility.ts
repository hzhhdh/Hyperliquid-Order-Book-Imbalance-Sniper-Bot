export function isEligibleForStaking(address: string, chain: string, amount: number): boolean {
  return isValidAddress(address, chain) && validateStakeAmount(amount, 0.01, 1000000);
}
