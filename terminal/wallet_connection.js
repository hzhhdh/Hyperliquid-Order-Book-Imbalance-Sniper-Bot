// React + ethers.js
import { ethers } from 'ethers';

function ConnectWallet() {
  const connect = async () => {
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    await provider.send("eth_requestAccounts", []);
    const signer = provider.getSigner();
    const address = await signer.getAddress();
    console.log('Connected:', address);
  };

  return <button onClick={connect}>Connect Wallet</button>;
}
