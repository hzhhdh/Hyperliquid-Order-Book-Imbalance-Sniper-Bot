import { ethers } from 'ethers';
import { Logger `logger` from '../utils/logger';

interface StakingData {
    slashingRisk: number;
    stakedAmount: ethers.BigNumber;
}

class EigenLayerSlashingProtection {
    private provider: ethers.providers.JsonRpcProvider;
    private contract: ethers.Contract;

    constructor(providerUrl: string, contractAddress: string) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.contract = new ethers.Contract(contractAddress, ['function getStakingData() view returns (uint256, uint256)'], this.provider);
    }

    async checkSlashingRisk(): Promise<StakingData> {
        try {
            const [slashingRisk, stakedAmount] = await this.contract.getStakingData();
            return { slashingRisk: slashingRisk.toNumber(), stakedAmount };
        } catch (error) {
            logger.error(`Error checking slashing risk: ${error}`);
            throw error;
        }
    }

    async protect(amount: ethers.BigNumber, threshold: number) {
        const data = await this.checkSlashingRisk();
        if (data.slashingRisk > threshold) {
            // TODO: Withdraw or adjust stake
            logger.warn(`High slashing risk: ${data.slashingRisk}`);
        }
    }
}

export default EigenLayerSlashingProtection;
