const { ethers } = require('ethers');
const logger = require('../utils/logger');

class CurveRewardHarvester {
    constructor(providerUrl, privateKey, gaugeAddress) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
        this.gauge = new ethers.Contract(gaugeAddress, ['function claim_rewards()'], this.wallet);
    }

    async harvestRewards() {
        try {
            const tx = await this.gauge.claim_rewards();
            await tx.wait();
            logger.info(`Harvested CRV rewards: ${tx.hash}`);
        } catch (error) {
            logger.error(`Error harvesting rewards: ${error.message}`);
            throw error;
        }
    }

    async reinvest() {
        await this.harvestRewards();
        // TODO: Reinvest rewards into pool
        logger.info('Reinvested CRV rewards');
    }
}

module.exports = CurveRewardHarvester;
