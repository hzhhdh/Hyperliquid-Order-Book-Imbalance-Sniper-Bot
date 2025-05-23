export async function optimizePools(chains: string[]): Promise<string[]> {
  const pools = await Promise.all(chains.map(chain => getPoolData(chain)));
  return pools.sort((a, b) => b.apy - a.apy).map(p => p.id);
}
