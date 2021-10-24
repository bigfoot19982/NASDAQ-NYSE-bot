from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Напиши, пожалуйста тикер компании,"
        f" данные которой тебе интересны. Напиши все буквы либо в нижнем, либо в верхнем регистре.")
