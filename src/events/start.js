const { Markup } = require("telegraf");
const { createUser } = require("../database/functions");
const { adminIds } = require("../configs");
const { mainMenuKeyboard } = require("../keyboards");

async function startCommand(ctx) {
  try {
    const telegramId = ctx.from.id;
    const firstName = ctx.from.first_name || "بدون نام";

    await createUser({ telegramId, firstName });

    if (adminIds.includes(telegramId)) {
      await ctx.reply(
        `سلام ادمین عزیز ${firstName}! خوش اومدی.`,
        Markup.keyboard(mainMenuKeyboard.admin).resize()
      );
    } else {
      await ctx.reply(
        `سلام ${firstName}! خوش اومدی به ربات.`,
        Markup.keyboard(mainMenuKeyboard.user).resize()
      );
    }
  } catch (error) {
    console.error("Error in startCommand:", error.message);
  }
}

module.exports = startCommand;
