from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="شروع"),
            KeyboardButton(text="راهنما")
        ]
    ],
    resize_keyboard=True
)
