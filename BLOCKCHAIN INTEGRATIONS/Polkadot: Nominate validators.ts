import { ApiPromise, WsProvider } from '@polkadot/api';
export async function nominatePolkadot(validators: string[]): Promise<string> {
  const provider = new WsProvider('wss://rpc.polkadot.io');
  const api = await ApiPromise.create({ provider });
  try {
    const tx = api.tx.staking.nominate(validators);
    const txId = generateTxId();
    logInfo(`Nominated validators on Polkadot: ${txId}`);
    return txId;
  } catch (error) {
    throw new Error(`Polkadot nomination failed: ${error.message}`);
  }
}
