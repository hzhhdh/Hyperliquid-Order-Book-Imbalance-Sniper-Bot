async function approveToken(
  tokenAddress: string,
  amount: ethers.BigNumberish
) {
  const token = new ethers.Contract(tokenAddress, ERC20_ABI, wallet);
  const tx = await token.approve(PANCAKE_ROUTER_ADDRESS, amount);
  console.log(`Approval TX hash: ${tx.hash}`);
  await tx.wait();
  console.log('Tokens approved for router'); // now router can pull tokens :contentReference[oaicite:4]{index=4}
}
