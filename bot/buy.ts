async function buyToken(
  tokenOut: string,
  amountInWei: ethers.BigNumberish,
  slippageTolerance = 0.02
) {
  const path = [ethers.constants.AddressZero, tokenOut]; // BNB → token :contentReference[oaicite:5]{index=5}
  const amounts = await router.getAmountsOut(amountInWei, path);
  const amountOutMin = amounts[1]
    .mul(ethers.BigNumber.from(100 - slippageTolerance * 100))
    .div(100);

  const tx = await router.swapExactETHForTokensSupportingFeeOnTransferTokens(
    amountOutMin,
    path,
    wallet.address,
    Math.floor(Date.now() / 1000) + 60 * 2,        // 2-min deadline :contentReference[oaicite:6]{index=6}
    { value: amountInWei, gasLimit: 300_000 }
  );
  console.log(`Buy TX hash: ${tx.hash}`);
  const receipt = await tx.wait();
  console.log('Buy confirmed in block', receipt.blockNumber); :contentReference[oaicite:7]{index=7}
}
