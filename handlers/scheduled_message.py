from aiogram import Router, F, types
from bot import scheduler, bot


scheduler_router = Router()

@scheduler_router.message(F.text.startswith("напомни"))
async def process_notify(message: types.Message):
    scheduler.add_job(
        send_notification,
        "interval",
        seconds=5,
        kwargs={"chat_id": message.from_user.id},
    )
    await message.answer("Напоминание добавлено")

# напомни сходить в магазин
# напомни сделать ДЗ
async def send_notification(chat_id: int):
    await bot.send_message(
        chat_id=chat_id,
        text="Ваше напоминание"
    )