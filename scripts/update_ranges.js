task("update-ranges", "Updates Uniswap V3 liquidity ranges")
    .addParam("lower", "Lower tick")
    .addParam("upper", "Upper tick")
    .setAction(async (taskArgs, hre) => {
        const manager = await hre.ethers.getContract("LiquidityManager");
        await manager.adjustRange("0xTokenA", "0xTokenB", taskArgs.lower, taskArgs.upper);
    });
