const dotenv = require("dotenv");
dotenv.config();

const configs = {
  token: process.env.BOT_TOKEN,
  admin: process.env.ADMIN_ID,
  support: process.env.SUPPORT_ID,
  mongoUrl: process.env.MONGO_URL,
  channel: process.env.CHANNEL_ID,
  port: process.env.PORT || 3000,
};

module.exports = configs;
