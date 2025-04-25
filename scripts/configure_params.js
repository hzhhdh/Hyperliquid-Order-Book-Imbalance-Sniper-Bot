const { ethers } = require("hardhat");

async function configure() {
    const bot = await ethers.getContract("uniarb");
    await bot.setArbitrageThreshold(500); // 5% threshold
    console.log("Parameters configured");
}
