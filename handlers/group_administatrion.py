from aiogram import Router, F, types
from aiogram.filters import Command
from datetime import timedelta


group_administration_router = Router()


BAD_WORDS = ("дурак", "тупой")


@group_administration_router.message(Command("ban", prefix="/!", magic=True))
@group_administration_router.message(F.chat.type == "group")
async def ban_user(message: types.Message):
    print("Text:", message.text)
    admins = await message.chat.get_administrators()
    is_admin = message.reply_to_message.from_user.id in [admin.user.id for admin in admins]
    print()
    if message.reply_to_message:
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id,
            until_date=timedelta(seconds=45)
        )
        await message.answer(f"Был забанен @{message.reply_to_message.from_user.username}")


# @group_administration_router.message(Command("pin", prefix="/!", magic=True))
# @group_administration_router.message(F.chat.type == "group")
# async def pin_message(message: types.Message):
#     if message.reply_to_message:
#         await message.reply_to_message.pin()


# @group_administration_router.message(F.chat.type.in_(("group", "supergroup")))
# @group_administration_router.message(F.from_user.id.in_((12345678, 98765432)))
@group_administration_router.message((F.chat.type == "group") & (F.text))
# @group_administration_router.message(F.text)
async def catch_bad_words(message: types.Message):
    print("Chat type", message.chat.type)
    for word in BAD_WORDS:
        if word in message.text:
            await message.delete()
            await message.answer(f"Не матерись! @{message.from_user.username} использовал(а) запрещенное слово")
            break
