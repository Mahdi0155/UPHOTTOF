from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.main_menu import main_menu_keyboard

@dp.message_handler(commands=["start"], state="*")
async def start_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "سلام خوش اومدی!\nاز منوی زیر یکی رو انتخاب کن:", 
        reply_markup=main_menu_keyboard()
    )
