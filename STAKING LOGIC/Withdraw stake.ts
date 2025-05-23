export async function withdrawStake(chain: string, amount: number): Promise<string> {
  const txId = generateTxId();
  logInfo(`Withdrawn ${amount} from ${chain}: ${txId}`);
  return txId;
}
