task("execute-arbitrage", "Executes arbitrage between Uniswap and dYdX")
    .addParam("token", "Token address")
    .addParam("amount", "Amount in ETH")
    .setAction(async (taskArgs, hre) => {
        const bot = await hre.ethers.getContract("ManualMaxBot");
        await bot.executeStrategy(taskArgs.token, ethers.utils.parseEther(taskArgs.amount), 500);
    });
