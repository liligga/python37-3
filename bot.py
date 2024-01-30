from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()


async def set_commands():
    """
    Настройка команд 
     в меню бота
    """
    # строка выше наз-ся Docstring
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
        types.BotCommand(command="pic", description="Отправить картинку"),
        types.BotCommand(command="courses", description="Наши курсы"),
        types.BotCommand(command="lesson", description="Записаться на пробный урок"),
    ])