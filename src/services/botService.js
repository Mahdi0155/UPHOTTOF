const TelegramBot = require('node-telegram-bot-api');
const config = require('../../config/config');

const bot = new TelegramBot(config.telegramToken, { polling: true });

bot.on('message', (msg) => {
  console.log('New message:', msg.text);
});

module.exports = bot;
