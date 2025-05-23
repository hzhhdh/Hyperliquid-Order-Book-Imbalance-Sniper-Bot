export function formatCurrency(amount: number, currency: string): string {
  try {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency }).format(amount);
  } catch (error) {
    console.error(`Error formatting currency: ${error.message}`);
    return `${amount} ${currency}`;
  }
}
