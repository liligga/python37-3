import asyncio
from aiogram import types
import logging
from bot import bot, dp, set_commands, scheduler
from handlers import (
    start_router,
    pictures_router,
    courses_router,
    echo_router,
    free_lesson_reg_router,
    scheduler_router,
    group_administration_router
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
    dp.include_router(free_lesson_reg_router)
    dp.include_router(courses_router)
    dp.include_router(scheduler_router)
    dp.include_router(group_administration_router)
    
    # в самом конце
    dp.include_router(echo_router)

    #
    dp.startup.register(on_startup)

    scheduler.start()
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())