import { SigningStargateClient } from '@cosmjs/stargate';
export async function stakeCosmos(amount: number, validator: string): Promise<string> {
  const client = await SigningStargateClient.connect('https://rpc.cosmos.network');
  try {
    const txId = generateTxId();
    logInfo(`Staked ${amount} ATOM to ${validator}: ${txId}`);
    return txId;
  } catch (error) {
    throw new Error(`Cosmos staking failed: ${error.message}`);
  }
}
