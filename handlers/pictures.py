from aiogram import Router, types
from aiogram.filters import Command


pictures_router = Router()

@pictures_router.message(Command("pic"))
async def send_pic(message: types.Message):
    photo = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(photo=photo, caption="Довольный котик!")
