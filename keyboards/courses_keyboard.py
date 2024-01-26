from aiogram import types


def napravlenie_kb():
    # DRY Don't Repeat Yourself
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Бекенд"),
                types.KeyboardButton(text="Frontend")
            ],
            [
                types.KeyboardButton(text="iOS"),
                types.KeyboardButton(text="Android")
            ],
            [
                types.KeyboardButton(text="Тестирование"),
                types.KeyboardButton(text="Менеджмент проектов")
            ]
        ]
    )
    return kb
