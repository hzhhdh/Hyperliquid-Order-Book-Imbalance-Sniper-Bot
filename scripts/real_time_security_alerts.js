// Example: Telegram bot for security alerts
const TelegramBot = require('node-telegram-bot-api');
const bot = new TelegramBot('YOUR_TELEGRAM_BOT_TOKEN', { polling: true });

// Monitor for suspicious transactions
function monitorTransactions(transaction) {
    if (transaction.amount > 10000) { // $10k threshold
        bot.sendMessage(
            CHAT_ID,
            `🚨 Suspicious Activity: ${transaction.amount} $MOON moved to ${transaction.to}`
        );
    }
}
