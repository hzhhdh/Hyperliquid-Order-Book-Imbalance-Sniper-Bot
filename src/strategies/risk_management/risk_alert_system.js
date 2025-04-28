const { ethers } = require('ethers');
const axios = require('axios');
const logger = require('../utils/logger');

class RiskAlertSystem {
    constructor(providerUrl) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.cmcApi = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest';
    }

    async checkMarketRisk(tokenSymbol) {
        try {
            const response = await axios.get(this.cmcApi, {
                headers: { 'X-CMC_PRO_API_KEY': 'YOUR_API_KEY' },
                params: { symbol: tokenSymbol }
            });
            const volatility = response.data.data[tokenSymbol].quote.USD.percent_change_24h;
            return volatility > 10 || volatility < -10;
        } catch (error) {
            logger.error(`Error checking market risk for ${tokenSymbol}: ${error.message}`);
            throw error;
        }
    }

    async monitorPortfolio(wallet, tokens) {
        for (const token of tokens) {
            if (await this.checkMarketRisk(token)) {
                logger.warn(`High risk detected for ${token} in wallet ${wallet}`);
                // TODO: Send alert (e.g., email, push notification)
            }
        }
        logger.info(`Portfolio risk check completed for ${wallet}`);
    }
}

module.exports = RiskAlertSystem;
