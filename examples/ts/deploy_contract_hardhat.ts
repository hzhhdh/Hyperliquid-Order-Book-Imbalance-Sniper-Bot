import { ethers } from "hardhat";
async function main() {
  const Factory = await ethers.getContractFactory("Arbitrage");
  const arb = await Factory.deploy();
  console.log("Deployed at:", arb.address);
}
main();
