const bot = require('../services/botService');
const { findOrCreateUser } = require('../services/userService');

bot.onText(/\/start/, async (msg) => {
  const chatId = msg.chat.id;
  const firstName = msg.chat.first_name;
  const username = msg.chat.username;

  await findOrCreateUser(chatId, firstName, username);

  bot.sendMessage(chatId, 'به ربات خوش اومدی!');
});
