from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="گزینه 1", callback_data="option_1"),
            InlineKeyboardButton(text="گزینه 2", callback_data="option_2")
        ]
    ]
)
