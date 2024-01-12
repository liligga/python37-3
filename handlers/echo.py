from aiogram import Router, types


echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    await message.reply(f"Вы написали {message.text}")