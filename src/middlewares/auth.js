function isAdmin(ctx, next) {
  const adminIds = [123456789, 987654321]; // جایگزین کن با آیدی‌های واقعی
  if (adminIds.includes(ctx.from.id)) {
    return next();
  } else {
    return ctx.reply("⛔️ شما دسترسی ادمین ندارید.");
  }
}

module.exports = {
  isAdmin,
};
