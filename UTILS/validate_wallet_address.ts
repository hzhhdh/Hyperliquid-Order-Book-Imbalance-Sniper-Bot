export function isValidAddress(address: string, chain: string): boolean {
  const regexMap: { [key: string]: RegExp } = {
    eth: /^0x[a-fA-F0-9]{40}$/,
    ada: /^addr1[a-z0-9]{99}$/,
    sol: /^[1-9A-HJ-NP-Za-km-z]{32,44}$/,
    // Add patterns for other chains
  };
  return regexMap[chain]?.test(address) ?? false;
}
