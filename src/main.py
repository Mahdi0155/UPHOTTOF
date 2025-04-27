from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from config import TOKEN
from handlers import start, admin, user
import logging

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO)

# ساختن آبجکت‌های اصلی
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

# ثبت هندلرها
start.register_handlers_start(dp)
admin.register_handlers_admin(dp)
user.register_handlers_user(dp)

async def on_startup(dispatcher):
    print("ربات با موفقیت استارت شد.")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
