# Домашнее задание по теме "План написания админ панели"
# Задача "Продуктовая база"

import sqlite3


def initiate_db():
    # --- создание БД "not_telegram.db"
    cnt = sqlite3.connect("tlg_database.db")
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

    cnt.commit()
    cnt.close()


def add_product():  # --- заполнение БД только уникальными записями
    cnt = sqlite3.connect("tlg_database.db")
    cur = cnt.cursor()

    # --- заполнение БД только уникальными записями, 4 записи
    for i in range(1, 5):
        check = cur.execute("SELECT * FROM Products WHERE title = ?", (f"Витамин {i} из БД",))

        if check.fetchone() is None:
            with open(f"product_{i}.jpg", "rb") as img_file:
                photo = sqlite3.Binary(img_file.read())
            cur.execute("INSERT INTO Products (title, description, price, image) VALUES (?, ?, ?, ?)",
                        (f"Витамин {i} из БД", f"Вкусный витамин {i} из БД", f"{i * 100}", photo))

    cnt.commit()
    cnt.close()


def get_all_products():  # выводит все записи на консоль
    cnt = sqlite3.connect("tlg_database.db")
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
