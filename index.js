const solanaWeb3 = require('@solana/web3.js');
const axios = require('axios');
const TelegramBot = require('node-telegram-bot-api');
const config = require('./config.json');

// Initialize Solana connection
const connection = new solanaWeb3.Connection(config.solanaRpcUrl);

// Initialize Telegram bot
const bot = new TelegramBot(config.security.telegramBotToken, { polling: true });

// Function to monitor transactions
async function monitorTransactions() {
    const latestBlockhash = await connection.getLatestBlockhash();
    const transactions = await connection.getConfirmedSignaturesForAddress2(
        new solanaWeb3.PublicKey(config.dexPools[0].address), // Monitor Raydium pool
        {
            limit: 10,
        }
    );

    for (const tx of transactions) {
        const transaction = await connection.getConfirmedTransaction(tx.signature);

        // Check for suspicious transactions
        if (transaction.meta.postBalances[0] - transaction.meta.preBalances[0] > config.security.suspiciousAmountThreshold) {
            bot.sendMessage(
                config.security.telegramChatId,
                `🚨 Suspicious Transaction: ${transaction.transaction.signatures[0]}`
            );
        }
    }
}

// Function to rebalance pools
async function rebalancePools() {
    const poolData = await axios.get(`https://api.birdeye.so/defi/pools?apiKey=${config.analytics.birdeyeApiKey}`);

    // Logic to rebalance pools based on weights in config.json
    const raydiumPool = config.dexPools.find(pool => pool.name === "Raydium");
    const orcaPool = config.dexPools.find(pool => pool.name === "Orca");

    console.log(`Rebalancing ${raydiumPool.weight}% to Raydium and ${orcaPool.weight}% to Orca...`);
}

// Run tasks
monitorTransactions();
rebalancePools();
