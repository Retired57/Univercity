# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."
# Задача "Первые пользователи"

import sqlite3

# --- создание БД "not_telegram.db"
ctn = sqlite3.connect("not_telegram.db")
cr = ctn.cursor()

cr.execute("""
    CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

# --- заполнение БД, 10 записей
for i in range(1, 11):
    cr.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
               (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

# --- меняем баланс на 500 у каждого второго, начиная с 1-й записи
cr.execute("UPDATE Users SET balance = ? WHERE id % 2 = ?", ("500", 1))

# удаляем каждую третью запись, начиная с 1-й записи
cr.execute("DELETE FROM Users WHERE (id + 3 ) % 3 = ?", (1,))

# отбираем записи без id, в которых age != 60
cr.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

# выводим отобранные записи на консоль
new_cr = cr.fetchall()
for user in new_cr:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

ctn.commit()
ctn.close()
