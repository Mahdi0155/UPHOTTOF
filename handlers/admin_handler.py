from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.admin_panel import admin_panel_menu
from states.admin_states import AdminState

@dp.message_handler(commands=['admin'], state="*")
async def admin_panel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("وارد پنل مدیریت شدید.", reply_markup=admin_panel_menu)
    await AdminState.main_menu.set()
