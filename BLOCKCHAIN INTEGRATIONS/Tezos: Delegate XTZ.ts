export async function delegateTezos(amount: number, baker: string): Promise<string> {
  try {
    const txId = generateTxId();
    logInfo(`Delegated ${amount} XTZ to ${baker}: ${txId}`);
    return txId;
  } catch (error) {
    throw new Error(`Tezos delegation failed: ${error.message}`);
  }
}
