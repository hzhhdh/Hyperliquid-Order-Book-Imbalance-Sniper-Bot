async function sellToken(
  tokenIn: string,
  amountIn: ethers.BigNumberish,
  slippageTolerance = 0.02
) {
  // ensure allowance first
  await approveToken(tokenIn, amountIn);

  const path = [tokenIn, ethers.constants.AddressZero]; // token → BNB
  const amounts = await router.getAmountsOut(amountIn, path);
  const amountOutMin = amounts[1]
    .mul(ethers.BigNumber.from(100 - slippageTolerance * 100))
    .div(100);

  const tx = await router.swapExactTokensForETHSupportingFeeOnTransferTokens(
    amountIn,
    amountOutMin,
    path,
    wallet.address,
    Math.floor(Date.now() / 1000) + 60 * 2,
    { gasLimit: 300_000 }
  );
  console.log(`Sell TX hash: ${tx.hash}`);
  const receipt = await tx.wait();
  console.log('Sell confirmed in block', receipt.blockNumber); :contentReference[oaicite:8]{index=8}
}
