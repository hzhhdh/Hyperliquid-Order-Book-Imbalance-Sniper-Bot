const { ethers } = require('ethers');
const logger = require('../utils/logger');

class CompoundBorrowMonitor {
    constructor(providerUrl, privateKey, cometAddress) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
        this.comet = new ethers.Contract(cometAddress, ['function getBorrowHealth(address) view returns (uint256)'], this.wallet);
    }

    async checkHealth(userAddress) {
        try {
            const healthFactor = await this.comet.getBorrowHealth(userAddress);
            if (healthFactor.lt(ethers.utils.parseEther('1.5'))) {
                logger.warn(`Low health factor for ${userAddress}: ${healthFactor}`);
            }
            return healthFactor;
        } catch (error) {
            logger.error(`Error checking health: ${error.message}`);
            throw error;
        }
    }
}

module.exports = CompoundBorrowMonitor;
