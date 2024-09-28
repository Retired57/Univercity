# Домашнее задание по теме "Клавиатура кнопок".
# Задача "Меньше текста, больше кликов"

from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

import asyncio

router = Router()

start_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Рассчитать"),
               KeyboardButton(text="Информация"),
               KeyboardButton(text="Выход")]],
    resize_keyboard=True
)

menu_off = ReplyKeyboardRemove()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=start_menu)


@router.message(Command("finish"))  # окончание работы бота
async def cmd_finish(message: Message):
    await message.answer("Бот завершил свою работу.", reply_markup=menu_off)
    print("Бот завершил свою работу.")
    await dp.stop_polling()


@router.message(F.text == "Выход")  # начало опроса
async def cmd_finish(message: Message):
    await message.answer("Бот завершил свою работу.", reply_markup=menu_off)
    print("Бот завершил свою работу.")
    await dp.stop_polling()


@router.message(F.text == "Информация")  # начало опроса
async def cmd_finish(message: Message):
    await message.answer("Это мой бот, который создан в результате выполнения домашнего задания по модулю 13.")
    print("Это мой бот, который создан в результате выполнения домашнего задания по модулю 13.")


# @router.message(F.text.lower() == "calories")  # начало опроса
@router.message(F.text == "Рассчитать")  # начало опроса
async def set_age(message: Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@router.message(F.text, UserState.age)
async def set_growth(message: Message, state: FSMContext):
    check = message.text  # простейшая проверка корректности возраста
    if not int(check) or not (5 <= int(check) <= 100):
        await message.reply("Введите корректное число от 5 до 100:")
        return
    await state.update_data(age=check)

    await message.answer("Введите свой рост в сантиметрах:")
    await state.set_state(UserState.growth)


@router.message(F.text, UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    check = message.text  # простейшая проверка корректности роста
    if not int(check) or not (50 <= int(check) <= 250):
        await message.reply("Введите корректное число от 50 до 250:")
        return
    await state.update_data(growth=check)

    await message.answer("Введите свой вес в килограммах:")
    await state.set_state(UserState.weight)


@router.message(F.text, UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    check = message.text  # простейшая проверка корректности веса
    if not int(check) or not (20 <= int(check) <= 200):
        await message.reply("Введите корректное число от 20 до 200:")
        return
    await state.update_data(weight=check)

    data = await state.get_data()  # чтение из БД
    calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5
    await state.clear()  # это вместо state.finish() в старой версии
    await message.answer(f"Вам нужно {calories} килокалорий в сутки.", reply_markup=start_menu)


@router.message()
async def msg_any(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")
    print("Введите команду /start, чтобы начать общение.")


# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Updates were skipped successfully.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    my_token = " -= Your TOKEN must be here! =- "  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    bot = Bot(token=my_token)
    dp = Dispatcher(storage=MemoryStorage())
    asyncio.run(main())