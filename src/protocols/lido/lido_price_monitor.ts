import { ethers } from 'ethers';
import { Logger } from '../utils/logger';

interface PriceData {
    price: ethers.BigNumber;
    timestamp: number;
}

class LidoPriceMonitor {
    private provider: ethers.providers.JsonRpcProvider;
    private chainlink: ethers.Contract;
    private logger: Logger;

    constructor(providerUrl: string, chainlinkAddress: string) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.chainlink = new ethers.Contract(chainlinkAddress, ['function latestAnswer() view returns (uint256)'], this.provider);
        this.logger = new Logger('LidoPriceMonitor');
    }

    async getPrice(): Promise<PriceData> {
        try {
            const price = await this.chainlink.latestAnswer();
            return { price, timestamp: Date.now() };
        } catch (error) {
            this.logger.error(`Error fetching price: ${error}`);
            throw error;
        }
    }

    async monitor(threshold: number) {
        const data = await this.getPrice();
        if (data.price.gt(ethers.utils.parseEther(threshold.toString()))) {
            this.logger.warn(`Arbitrage opportunity: stETH/ETH price ${data.price}`);
        }
    }
}

export default LidoPriceMonitor;
