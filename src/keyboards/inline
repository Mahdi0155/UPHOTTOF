from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# کیبورد تأیید یا لغو
confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ تایید", callback_data="confirm"),
            InlineKeyboardButton(text="❌ لغو", callback_data="cancel")
        ]
    ]
)

# کیبورد پنل مدیریت
admin_panel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="➕ افزودن محصول", callback_data="add_product")],
        [InlineKeyboardButton(text="🗑️ حذف محصول", callback_data="delete_product")],
        [InlineKeyboardButton(text="📋 لیست محصولات", callback_data="list_products")]
    ]
)
