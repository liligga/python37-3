import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from pprint import pprint


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("pic"))
async def send_pic(message: types.Message):
    photo = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(photo=photo, caption="Довольный котик!")

# обработка команды
# handler
@dp.message(Command("start"))
async def start(message: types.Message):
    pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())