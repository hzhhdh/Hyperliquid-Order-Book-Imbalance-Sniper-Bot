export function validateStakeAmount(amount: number, min: number, max: number): boolean {
  return amount >= min && amount <= max;
}
