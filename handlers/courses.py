from aiogram import Router, F, types
from aiogram.filters import Command
from db.queries import get_courses

courses_router = Router()

@courses_router.message(Command("courses"))
async def show_courses(message: types.Message):
    courses = get_courses()
    buttons = list(map())
    # keyboard
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            # [
            #     types.KeyboardButton(text="Python"),
            #     types.KeyboardButton(text="Frontend"),
            # ],
            # [
            #     types.KeyboardButton(text="Android"),
            #     types.KeyboardButton(text="iOS"),
            # ],
            # [
            #     types.KeyboardButton(text="Тестирование"),
            # ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите направление:", reply_markup=kb)


@courses_router.message(F.text.lower() == "python")
async def about_python(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("Курс по Python", reply_markup=kb)
