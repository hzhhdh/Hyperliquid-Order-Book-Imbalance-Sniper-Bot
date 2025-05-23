import { Contract } from 'ethers';
export async function stakeEthLido(amount: number, wallet: ethers.Wallet): Promise<string> {
  const lidoContractAddress = '0x...'; // Lido contract address
  const lidoAbi = []; // Lido ABI
  const contract = new Contract(lidoContractAddress, lidoAbi, wallet);
  try {
    const tx = await contract.submit({ value: ethers.utils.parseEther(amount.toString()) });
    await tx.wait();
    logInfo(`Staked ${amount} ETH on Lido: ${tx.hash}`);
    return tx.hash;
  } catch (error) {
    throw new Error(`Lido staking failed: ${parseBlockchainError(error)}`);
  }
}
