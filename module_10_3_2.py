# Домашнее задание по теме "Блокировки и обработка ошибок"
# Задача "Банковские операции"

# Вариант 2 (ЖЕСТКИЙ):
#                       После отклонения запроса на снятие и блокировки потока 2,
#                       разблокировка потока 2 и разрешение на попытки снятия средств
#                       наступят только после увеличения баланса >= 500

# from threading import Thread, Lock
import threading
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 101):
            random_number = randint(50, 500)
            self.balance += random_number
            print(f"Пополнение: {random_number}. Баланс: {self.balance}")
            if (self.balance >= 500) and self.lock.locked():
                while self.lock.locked():
                    self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(1, 101):
            with self.lock:
                random_number = randint(50, 500)
                print(f"запрос на {random_number}.")
                if random_number <= self.balance:
                    self.balance -= random_number
                    print(f"Снятие: {random_number}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонен, недостаточно средств - {self.balance}")
                    self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

# Вывод на консоль (может отличаться значениями, логика должна быть та же):
# ==========================================================================

# Пополнение: 241. Баланс: 241
# Запрос на 174
# Снятие: 174. Баланс: 67
# Пополнение: 226. Баланс: 293
# Запрос на 421
# Запрос отклонён, недостаточно средств
# Пополнение: 133. Баланс: 426
# Запрос на 422
# Снятие: 422. Баланс: 4
# Пополнение: 150. Баланс: 154
# Запрос на 207
# Запрос отклонён, недостаточно средств
# ....
# Запрос на 431
# Снятие: 431. Баланс: 276
# Запрос на 288
# Запрос отклонён, недостаточно средств
# Итоговый баланс: 276

