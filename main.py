import asyncio
from aiogram import types
import logging
from bot import bot, dp, set_commands
from handlers import (
    start_router,
    pictures_router,
    counrses_router,
    echo_router
)


async def main():
    await set_commands()
    dp.include_router(start_router)
    dp.include_router(pictures_router)
    dp.include_router(counrses_router)
    
    # в самом конце
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())