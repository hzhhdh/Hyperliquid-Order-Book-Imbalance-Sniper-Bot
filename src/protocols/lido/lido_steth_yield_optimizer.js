const { ethers } = require('ethers');
const axios = require('axios');
const logger = require('../utils/logger');

class LidoStETHYieldOptimizer {
    constructor(providerUrl, privateKey) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
        this.inchApi = 'https://api.1inch.io/v5.0/1';
    }

    async allocateStETH(amount, targetProtocol) {
        const quote = await axios.get(`${this.inchApi}/swap`, {
            params: { fromTokenAddress: '0x...', toTokenAddress: targetProtocol, amount }
        });
        const tx = {
            to: quote.data.to,
            data: quote.data.data,
            value: quote.data.value || 0,
        };
        const signedTx = await this.wallet.signTransaction(tx);
        const txResponse = await this.provider.sendTransaction(signedTx);
        logger.info(`Allocated stETH to ${targetProtocol}: ${txResponse.hash}`);
    }
}

module.exports = LidoStETHYieldOptimizer;
