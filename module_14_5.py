# Домашнее задание по теме "Написание примитивной ORM"
# Задача "Регистрация покупателей"

import crud_functions_2 as cf

from aiogram import Bot, Dispatcher
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

import sqlite3
import asyncio

router = Router()

start_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Регистрация")],
              [KeyboardButton(text="Рассчитать"),
               KeyboardButton(text="Информация"),
               KeyboardButton(text="Выход")],
              [KeyboardButton(text="Купить")]],
    resize_keyboard=True
)

menu_off = ReplyKeyboardRemove()

inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Расчёт калорий", callback_data="calories"),
                      InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas"),
                      InlineKeyboardButton(text="Выход", callback_data="exit")]]
)

inline_buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Product1", callback_data="product_buying"),
                      InlineKeyboardButton(text="Product2", callback_data="product_buying"),
                      InlineKeyboardButton(text="Product3", callback_data="product_buying"),
                      InlineKeyboardButton(text="Product4", callback_data="product_buying"),
                      InlineKeyboardButton(text="Выход", callback_data="exit")]]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

    def __init__(self):
        self.balance = 1000


@router.message(CommandStart())
async def cmd_start(message: Message):
    print("Привет! Я бот помогающий твоему здоровью.")
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=start_menu)


@router.message(Command("finish"))  # окончание работы бота
async def cmd_finish(message: Message):
    await message.answer("Бот завершил свою работу.", reply_markup=menu_off)
    print("Бот завершил свою работу.")
    await dp.stop_polling()


@router.message(F.text == "Выход")  # пункт меню, окончание работы бота
async def cmd_finish2(message: Message):
    await message.answer("Бот завершил свою работу.", reply_markup=menu_off)
    print("Бот завершил свою работу.")
    await dp.stop_polling()


@router.message(F.text == "Купить")  # пункт меню, переход к новому инлайн-меню
async def get_buying_list(message: Message):
    cnt = sqlite3.connect("tlg_db.db")

    cur = cnt.cursor()
    cur.execute("SELECT * FROM Products")
    new_cur = cur.fetchall()
    for user in new_cur:
        with open("ph.jpg", "wb") as f:
            f.write(user[4])
        img = FSInputFile("ph.jpg")
        await message.answer_photo(img, f"Название: {user[1]} | Описание: {user[2]} | Цена: {user[3]}",
                                   reply_markup=menu_off)

    cnt.commit()
    cnt.close()
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_buy_menu)


@router.message(F.text == "Информация")  # пункт меню
async def cmd_finish(message: Message):
    await message.answer("Это мой бот, который создан в результате выполнения домашнего задания по модулю 13.")
    print("Это мой бот, который создан в результате выполнения домашнего задания по модулю 13.")


@router.message(F.text == "Рассчитать")  # пункт меню, начало опроса
async def main_menu(message: Message):
    await message.answer("Выберите опцию:", reply_markup=inline_menu)


@router.callback_query(F.data == "product_buying")  # формулы для расчета калорий
async def send_confirm_message(call: CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!", reply_markup=start_menu)
    await call.answer()


@router.callback_query(F.data == "exit")  # выход из программы
async def btn_finish(call: CallbackQuery):
    await call.message.answer("Бот завершил свою работу.", reply_markup=menu_off)
    await call.answer()
    print("Бот завершил свою работу.")
    await dp.stop_polling()


@router.callback_query(F.data == "formulas")  # формулы для расчета калорий
async def set_age(call: CallbackQuery):
    await call.message.answer("Упрощенный вариант формулы Миффлина-Сан Жеора:\n \
    (М): 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n \
    (Ж): 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")
    await call.answer()


# --- начало цепочки опроса для расчета калорий (изменение состояний) ---
@router.callback_query(F.data == "calories")  # начало опроса
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст:", reply_markup=menu_off)
    await call.answer()
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


# --- окончание цепочки опроса для расчета калорий (изменение состояний) ---


# --- начало новой цепочки опроса для регистрации пользователей (изменение состояний) ---
@router.message(F.text == "Регистрация")  # пункт меню, начало опроса
async def sign_up(message: Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит):", reply_markup=menu_off)
    await state.set_state(RegistrationState.username)


@router.message(F.text, RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    if cf.is_user_included(message.text):
        await message.answer("Такой пользователь уже существует, введите другое имя.")
        await message.answer("Введите новое имя пользователя (только латинский алфавит):")
        await state.set_state(RegistrationState.username)
    else:
        await state.update_data(username=message.text)
        await message.answer("Введите свой email:")
        await state.set_state(RegistrationState.email)


@router.message(F.text, RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)


@router.message(F.text, RegistrationState.age)
async def set_age(message: Message, state: FSMContext):
    check = message.text  # простейшая проверка корректности возраста
    if not int(check) or not (15 <= int(check) <= 100):
        await message.reply("Введите корректное число от 15 до 100:")
        return
    await state.update_data(age=check)

    data = await state.get_data()
    username = data.get("username")
    email = data.get("email")
    age = data.get("age")

    print(f"{username}, {email}, {age}")
    cf.add_user(username, email, age)

    await state.clear()  # это вместо state.finish() в старой версии
    await message.answer(f"Пользователь {username} зарегистрирован.", reply_markup=start_menu)


# --- окончание новой цепочки опроса для регистрации пользователей (изменение состояний) ---


@router.message()
async def msg_any(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")
    print("Введите команду /start, чтобы начать общение.")


# Запуск процесса поллинга новых апдейтов
async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    print("Updates were skipped successfully.")
    cf.get_all_products()
    await dp.start_polling(bot)


if __name__ == "__main__":
    my_token = " -= Your TOKEN must be here! =- "  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    bot = Bot(token=my_token)
    dp = Dispatcher(storage=MemoryStorage())
    asyncio.run(main())
