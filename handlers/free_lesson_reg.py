from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


free_lesson_reg_router = Router()
# FSM - Finite State Machine
# Конечный автомат
class FreeLessonReg(StatesGroup):
    name = State()
    age = State()
    napravlenie = State()
    phone = State()

def napravlenie_kb():
    # DRY Don't Repeat Yourself
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Backend"),
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

@free_lesson_reg_router.message(Command("lesson"))
async def start_registration(message: types.Message, state: FSMContext):
    await state.set_state(FreeLessonReg.name)
    await message.answer("Предлагаем Вам записаться на бесплатный урок! Можете остановить регистрацию командой /cancel")
    await message.answer("Как Вас зовут?")


@free_lesson_reg_router.message(Command("cancel"))
@free_lesson_reg_router.message(F.text.lower() == "отмена")
async def cancel_registration(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Регистрация отменена")


@free_lesson_reg_router.message(FreeLessonReg.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FreeLessonReg.age)
    await message.answer("Сколько Вам лет?")


@free_lesson_reg_router.message(FreeLessonReg.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом")
    elif int(message.text) < 14 or int(message.text) > 80:
        await message.answer("Возраст должен быть от 14 до 80 лет")
    else:
        age = int(message.text)
        await state.update_data(age=age)
        await state.set_state(FreeLessonReg.napravlenie)
        await message.answer("Какое направление Вы хотите изучать?", reply_markup=napravlenie_kb())


@free_lesson_reg_router.message(FreeLessonReg.napravlenie)
async def process_napravlenie(message: types.Message, state: FSMContext):
    await state.update_data(napravlenie=message.text)
    hide_kb = types.ReplyKeyboardRemove()
    await state.set_state(FreeLessonReg.phone)
    await message.answer("Ваш номер телефона?", reply_markup=hide_kb)


@free_lesson_reg_router.message(FreeLessonReg.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()
    await message.answer(f"Ваши данные: {data}")
    await message.answer("Спасибо за регистрацию! Мы с Вами свяжемся")
    # Save To DataBase (DB)
    # очистка состояний
    await state.clear()