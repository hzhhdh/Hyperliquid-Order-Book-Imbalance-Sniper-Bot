import { ethers } from 'ethers';
import { Logger } from '../utils/logger';

interface VaultData {
    apy: number;
    tvl: ethers.BigNumber;
}

class YearnVaultMonitor {
    private provider: ethers.providers.JsonRpcProvider;
    private vault: ethers.Contract;
    private logger: Logger;

    constructor(providerUrl: string, vaultAddress: string) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.vault = new ethers.Contract(vaultAddress, ['function getVaultData() view returns (uint256, uint256)'], this.provider);
        this.logger = new Logger('YearnVaultMonitor');
    }

    async fetchVaultData(): Promise<VaultData> {
        try {
            const [apy, tvl] = await this.vault.getVaultData();
            return { apy: apy.toNumber(), tvl };
        } catch (error) {
            this.logger.error(`Error fetching vault data: ${error}`);
            throw error;
        }
    }

    async monitor(threshold: number) {
        const data = await this.fetchVaultData();
        if (data.apy < threshold) {
            this.logger.warn(`Low APY detected: ${data.apy}%`);
        }
    }
}

export default YearnVaultMonitor;
