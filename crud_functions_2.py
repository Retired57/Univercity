# Домашнее задание по теме "Написание примитивной ORM"
# Задача "Регистрация покупателей"

import sqlite3


def initiate_db():
    # --- создание БД "tlg_db.db"
    cnt = sqlite3.connect("tlg_db.db")
    cur = cnt.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    image BLOB NOT NULL
    )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)

    cnt.commit()
    cnt.close()


def is_product_included(name):
    cnt = sqlite3.connect("tlg_db.db")
    cur = cnt.cursor()

    check = cur.execute("SELECT * FROM Products WHERE title = ?", (name,))
    ret = True
    if check.fetchone() is None:
        ret = False

    cnt.commit()
    cnt.close()
    return ret


def add_product():  # --- заполнение БД только уникальными записями
    cnt = sqlite3.connect("tlg_db.db")
    cur = cnt.cursor()

    # --- заполнение БД только уникальными записями, 4 записи
    for i in range(1, 5):
        if not is_product_included(f"Витамин {i} из БД"):
            with open(f"product_{i}.jpg", "rb") as img_file:
                photo = sqlite3.Binary(img_file.read())
            cur.execute("INSERT INTO Products (title, description, price, image) VALUES (?, ?, ?, ?)",
                        (f"Витамин {i} из БД", f"Вкусный витамин {i} из БД", f"{i * 100}", photo))

    cnt.commit()
    cnt.close()


def is_user_included(username):
    cnt = sqlite3.connect("tlg_db.db")
    cur = cnt.cursor()

    check = cur.execute("SELECT * FROM Users WHERE username = ?", (username,))
    ret = True
    if check.fetchone() is None:
        ret = False

    cnt.commit()
    cnt.close()
    return ret


def add_user(username, email, age):  # --- заполнение БД только уникальными записями
    cnt = sqlite3.connect("tlg_db.db")
    cur = cnt.cursor()

    # --- заполнение БД только уникальными записями, 4 записи
    if not is_user_included(username):
        cur.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                    (username, email, age, 1000))

    cnt.commit()
    cnt.close()


def get_all_products():  # выводит все записи на консоль
    cnt = sqlite3.connect("tlg_db.db")
    cur = cnt.cursor()

    # отбираем все записи
    cur.execute("SELECT * FROM Products")
    # выводим отобранные записи на консоль
    new_cur = cur.fetchall()
    for user in new_cur:
        print(f"{user[0]} | Продукт: {user[1]} | Описание: {user[2]} | Цена: {user[3]}")

    cnt.commit()
    cnt.close()

# initiate_db()
# add_product()
# get_all_products()
