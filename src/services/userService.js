const User = require('../models/user');

async function findOrCreateUser(telegramId, firstName, username) {
  let user = await User.findOne({ telegramId });
  if (!user) {
    user = await User.create({ telegramId, firstName, username });
  }
  return user;
}

module.exports = { findOrCreateUser };
