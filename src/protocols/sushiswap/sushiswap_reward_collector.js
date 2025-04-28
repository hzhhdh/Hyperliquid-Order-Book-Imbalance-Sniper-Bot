const { ethers } = require('ethers');
const logger = require('../utils/logger');

class SushiSwapRewardCollector {
    constructor(providerUrl, privateKey, masterchefAddress) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
        this.masterchef = new ethers.Contract(masterchefAddress, ['function harvest(uint256)'], this.wallet);
    }

    async collectRewards(poolId) {
        try {
            const tx = await this.masterchef.harvest(poolId);
            await tx.wait();
            logger.info(`Collected SUSHI rewards for pool ${poolId}: ${tx.hash}`);
        } catch (error) {
            logger.error(`Error collecting rewards: ${error.message}`);
            throw error;
        }
    }
}

module.exports = SushiSwapRewardCollector;
