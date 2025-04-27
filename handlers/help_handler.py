from aiogram import types
from aiogram.dispatcher.filters import CommandHelp
from loader import dp

@dp.message_handler(CommandHelp())
async def show_help(message: types.Message):
    await message.answer("برای استفاده از ربات، از دکمه‌های موجود در منو استفاده کنید.")
