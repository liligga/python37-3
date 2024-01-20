import asyncio
from aiogram import types
import logging
from bot import bot, dp, set_commands
from handlers import (
    start_router,
    pictures_router,
    courses_router,
    echo_router,
    free_lesson_reg_router
)
from db.queries import init_db, create_tables, populate_db

async def on_startup(dispatcher):
    print('Бот вышел в онлайн')
    init_db()
    create_tables()
    populate_db()


async def main():
    await set_commands()
    dp.include_router(start_router)
    dp.include_router(pictures_router)
    dp.include_router(courses_router)
    dp.include_router(free_lesson_reg_router)
    
    # в самом конце
    dp.include_router(echo_router)

    #
    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())