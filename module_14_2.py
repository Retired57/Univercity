# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"
# Задача "Средний баланс пользователя"

import sqlite3

# --- создание БД "not_telegram.db"
ctn = sqlite3.connect("not_telegram_2.db")
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
cr.execute("DELETE FROM Users WHERE id % 3 = ?", (1,))

# удаляем запись с id = 6
cr.execute("DELETE FROM Users WHERE id = ?", (6,))

# подсчет кол-ва пользователей и суммы их балансов
cr.execute("SELECT COUNT(*) FROM Users")
total_users = cr.fetchone()[0]
cr.execute("SELECT SUM(balance) FROM Users")
all_balances = cr.fetchone()[0]

print(all_balances / total_users)  # вывод среднего баланса

ctn.commit()
ctn.close()
