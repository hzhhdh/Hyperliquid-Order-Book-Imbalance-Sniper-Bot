const { ethers } = require('ethers');
const logger = require('../utils/logger');

class YearnRewardHarvester {
    constructor(providerUrl, privateKey, vaultAddress) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
        this.vault = new ethers.Contract(vaultAddress, ['function harvest()'], this.wallet);
    }

    async harvest() {
        try {
            const tx = await this.vault.harvest();
            await tx.wait();
            logger.info(`Harvested Yearn rewards: ${tx.hash}`);
        } catch (error) {
            logger.error(`Error harvesting rewards: ${error.message}`);
            throw error;
        }
    }
}

module.exports = YearnRewardHarvester;
