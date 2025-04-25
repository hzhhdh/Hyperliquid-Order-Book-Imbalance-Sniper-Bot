const hre = require("hardhat");

async function main() {
    const [deployer] = await hre.ethers.getSigners();
    console.log("Deploying contracts with account:", deployer.address);

    // Deploy utilities
    const HoneypotChecker = await hre.ethers.getContractFactory("HoneypotChecker");
    const honeypotChecker = await HoneypotChecker.deploy();
    await honeypotChecker.deployed();

    // Deploy core contracts
    const uniarbbot = await hre.ethers.getContractFactory("ManualMaxBot");
    const bot = await uniarbbot.deploy(
        honeypotChecker.address,
        "0xUniswap", // Replace with actual address
        "0xdYdX"     // Replace with actual address
    );
    console.log("ManualMaxBot deployed to:", bot.address);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
