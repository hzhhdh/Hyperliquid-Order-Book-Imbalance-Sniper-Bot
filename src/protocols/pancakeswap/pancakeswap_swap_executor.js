const { ethers } = require('ethers');
const axios = require('axios');
const logger = require('../utils/logger');

class PancakeSwapExecutor {
    constructor(providerUrl, privateKey) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
        this.inchApi = 'https://api.1inch.io/v5.0/56'; // BSC chain ID
    }

    async executeSwap(fromToken, toToken, amount) {
        try {
            const quote = await axios.get(`${this.inchApi}/swap`, {
                params: { fromTokenAddress: fromToken, toTokenAddress: toToken, amount }
            });
            const tx = {
                to: quote.data.to,
                data: quote.data.data,
                value: quote.data.value || 0,
            };
            const signedTx = await this.wallet.signTransaction(tx);
            const txResponse = await this.provider.sendTransaction(signedTx);
            logger.info(`Swap executed on PancakeSwap: ${txResponse.hash}`);
        } catch (error) {
            logger.error(`Error executing swap: ${error.message}`);
            throw error;
        }
    }
}

module.exports = PancakeSwapExecutor;
