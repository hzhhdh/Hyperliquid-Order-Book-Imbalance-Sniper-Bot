import { ethers } from "ethers";

// RPC and wallet setup
const provider = new ethers.providers.JsonRpcProvider("https://mainnet.infura.io/v3/YOUR_INFURA_KEY");
const wallet = new ethers.Wallet("0xYOUR_PRIVATE_KEY", provider);

// ABI and contract address
const ERC20_ABI = [
  "function balanceOf(address) view returns (uint256)",
  "function transfer(address to, uint amount) returns (bool)"
];
const DAI_ADDRESS = "0x6B175474E89094C44Da98b954EedeAC495271d0F";
const dai = new ethers.Contract(DAI_ADDRESS, ERC20_ABI, wallet);

async function transferDai(to, amount) {
  const tx = await dai.transfer(to, ethers.utils.parseUnits(amount, 18));
  console.log("Sending DAI tx hash:", tx.hash);
  await tx.wait();
  console.log("DAI transfer confirmed");
}

transferDai('0xDef4567890abcdef1234567890abcdef12345678', '10.0');
