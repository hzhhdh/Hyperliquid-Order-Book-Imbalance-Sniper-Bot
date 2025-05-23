import { ethers } from 'ethers';
export async function connectMetaMask(): Promise<string | null> {
  if (!window.ethereum) throw new Error('MetaMask not installed');
  try {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    return accounts[0];
  } catch (error) {
    logInfo(`MetaMask connection failed: ${error.message}`);
    return null;
  }
}
