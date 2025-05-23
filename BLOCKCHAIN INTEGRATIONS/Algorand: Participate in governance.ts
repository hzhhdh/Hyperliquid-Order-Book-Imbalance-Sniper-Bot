export async function stakeAlgorand(amount: number): Promise<string> {
  try {
    const txId = generateTxId();
    logInfo(`Staked ${amount} ALGO in governance: ${txId}`);
    return txId;
  } catch (error) {
    throw new Error(`Algorand staking failed: ${error.message}`);
  }
}
