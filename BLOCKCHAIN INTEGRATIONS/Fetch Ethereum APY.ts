export async function getEthApy(): Promise<number> {
  return await retryOperation(async () => 5.2); // Fake APY
}
