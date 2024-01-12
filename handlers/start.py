from aiogram import Router, types
from aiogram.filters import Command
from pprint import pprint


start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    # обработка команды
    # handler
    pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}")