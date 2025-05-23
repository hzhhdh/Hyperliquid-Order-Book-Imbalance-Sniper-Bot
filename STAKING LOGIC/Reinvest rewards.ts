export async function reinvestRewards(chain: string, amount: number): Promise<string> {
  const txId = await retryOperation(() => stake(chain, amount));
  logInfo(`Reinvested ${amount} in ${chain}: ${txId}`);
  return txId;
}
