const { ethers } = require('ethers');
const axios = require('axios');
const logger = require('./utils/logger');

class UniswapSwapExecutor {
    constructor(providerUrl, privateKey) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
        this.inchApi = 'https://api.1inch.io/v5.0/1';
    }

    async getSwapQuote(fromToken, toToken, amount) {
        try {
            const response = await axios.get(`${this.inchApi}/swap`, {
                params: { fromTokenAddress: fromToken, toTokenAddress: toToken, amount }
            });
            return response.data;
        } catch (error) {
            logger.error(`Failed to fetch swap quote: ${error.message}`);
            throw error;
        }
    }

    async executeSwap(fromToken, toToken, amount) {
        const quote = await this.getSwapQuote(fromToken, toToken, amount);
        const tx = {
            to: quote.to,
            data: quote.data,
            value: quote.value || 0,
        };
        const signedTx = await this.wallet.signTransaction(tx);
        const txResponse = await this.provider.sendTransaction(signedTx);
        logger.info(`Swap executed: ${txResponse.hash}`);
        return txResponse;
    }
}

module.exports = UniswapSwapExecutor;
