export function handleStakingError(error: any): void {
  logInfo(`Staking error: ${parseBlockchainError(error)}`);
}
