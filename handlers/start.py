from aiogram import Router, F, types
from aiogram.filters import Command
from pprint import pprint


start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    # обработка команды
    # handler
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")                      
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/"),
                types.InlineKeyboardButton(text="Наш телеграм", url="https://t.me/geekskg"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
            ]
        ]
    )
    # pprint(message)
    await message.answer(f"Привет! {message.from_user.full_name}, ваш id: {message.from_user.id}", reply_markup=kb)


@start_router.callback_query(F.data == "about_us")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    
    await callback.message.answer("Здесь мы хотим рассказать о нашей компании")