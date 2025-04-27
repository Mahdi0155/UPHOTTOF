from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.user_panel import user_main_menu
from states.user_states import UserState

@dp.message_handler(commands=['start'], state="*")
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("سلام! به ربات خوش آمدید.", reply_markup=user_main_menu)
    await UserState.main_menu.set()

@dp.message_handler(text="بازگشت به منوی اصلی", state="*")
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await message.answer("بازگشت به منوی اصلی.", reply_markup=user_main_menu)
    await UserState.main_menu.set()
