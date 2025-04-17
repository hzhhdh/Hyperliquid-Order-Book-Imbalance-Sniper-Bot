import { ethers } from "ethers";
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
const router = new ethers.Contract(
  "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
  ["function swapExactETHForTokens(uint,address[],address,uint) payable returns (uint[])"],
  wallet
);

async function buyDAI() {
  const path = [
    ethers.constants.AddressZero, // WETH via native
    "0x6B175474E89094C44Da98b954EedeAC495271d0F" // DAI
  ];
  const tx = await router.swapExactETHForTokens(
    0,
    path,
    wallet.address,
    Math.floor(Date.now()/1000) + 300,
    { value: ethers.utils.parseEther("0.1") }
  );
  console.log("Uniswap V2 buy tx:", tx.hash);
}
buyDAI();
