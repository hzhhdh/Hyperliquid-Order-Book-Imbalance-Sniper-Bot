const { ethers } = require('ethers');
const axios = require('axios');
const logger = require('../utils/logger');

class CrossChainSwapExecutor {
    constructor(providerUrl, privateKey) {
        this.provider = new ethers.providers.JsonRpcProvider(providerUrl);
        this.wallet = new ethers.Wallet(privateKey, this.provider);
        this.wormholeApi = 'https://api.wormhole.com/v1/bridge';
    }

    async executeCrossChainSwap(srcChain, dstChain, fromToken, toToken, amount) {
        try {
            const quote = await axios.get(this.wormholeApi, {
                params: { srcChain, dstChain, fromToken, toToken, amount }
            });
            const tx = {
                to: quote.data.to,
                data: quote.data.data,
                value: quote.data.value || 0,
            };
            const signedTx = await this.wallet.signTransaction(tx);
            const txResponse = await this.provider.sendTransaction(signedTx);
            logger.info(`Cross-chain swap executed: ${txResponse.hash}`);
        } catch (error) {
            logger.error(`Error executing cross-chain swap: ${error.message}`);
            throw error;
        }
    }
}

module.exports = CrossChainSwapExecutor;
