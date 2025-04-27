import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize bot and dispatcher
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory database
files = {}

# Admins
ADMINS = [int(admin_id) for admin_id in os.getenv("ADMINS", "").split(",")]

# Upload limit (bytes)
UPLOAD_LIMIT = int(os.getenv("UPLOAD_LIMIT", 20971520))  # 20 MB default

# Handlers

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("سلام! فایل خودتو برام بفرست تا برات لینک بسازم.")

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def file_handler(message: types.Message):
    if not message.document:
        return

    if message.document.file_size > UPLOAD_LIMIT:
        await message.reply("فایل خیلی بزرگه. لطفا فایلی کوچیک‌تر از 20MB بفرستید.")
        return

    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path

    # ذخیره فایل در حافظه
    file_id = message.document.file_id
    files[file_id] = {
        "file_name": message.document.file_name,
        "file_size": message.document.file_size,
        "uploader_id": message.from_user.id,
        "upload_time": datetime.now()
    }

    link = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("مشاهده فایل", url=link)
    )

    await message.reply(
        f"فایل با موفقیت آپلود شد!\n\n"
        f"📄 نام فایل: {message.document.file_name}\n"
        f"📦 حجم فایل: {round(message.document.file_size/1024/1024, 2)} MB\n\n"
        f"برای مشاهده فایل روی دکمه زیر کلیک کنید:",
        reply_markup=keyboard
    )

@dp.message_handler(commands=["panel"])
async def panel_handler(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.reply("شما دسترسی به پنل ندارید.")
        return

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("📊 مشاهده آمار فایل‌ها", callback_data="stats"),
        InlineKeyboardButton("🗂 مشاهده همه فایل‌ها", callback_data="all_files")
    )

    await message.reply("به پنل مدیریت خوش اومدی!", reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == "stats")
async def stats_handler(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        f"📈 تعداد کل فایل‌های آپلود شده: {len(files)}"
    )

@dp.callback_query_handler(lambda call: call.data == "all_files")
async def all_files_handler(call: types.CallbackQuery):
    await call.answer()
    if not files:
        await call.message.edit_text("هیچ فایلی هنوز آپلود نشده!")
        return

    text = "📚 لیست فایل‌های آپلود شده:\n\n"
    for file_id, info in files.items():
        text += (
            f"📄 {info['file_name']} | "
            f"{round(info['file_size']/1024/1024, 2)} MB\n"
        )
    await call.message.edit_text(text)

# Run bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
