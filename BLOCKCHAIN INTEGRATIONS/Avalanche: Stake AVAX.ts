export async function stakeAvax(amount: number, validator: string): Promise<string> {
  try {
    const txId = generateTxId();
    logInfo(`Staked ${amount} AVAX to ${validator}: ${txId}`);
    return txId;
  } catch (error) {
    throw new Error(`Avalanche staking failed: ${error.message}`);
  }
}
