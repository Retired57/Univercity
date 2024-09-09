# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Задача "Потоки гостей в кафе"

from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    threads = []  # пустой список для потоков гостей

    def __init__(self, *tables_):
        self.tables = tables_
        self.queue = Queue()  # очередь для гостей - кафе работает, пока очередь не опустеет
        self.table_amount = len(self.tables)  # кол-во столов в кафе
        self.empty_tables = self.table_amount  # пустые столы - кафе работает, пока все столы не станут пустыми
        self.guests = None  # интерпретатор рекомендовал объявить эти атрибуты в методе __init__
        self.thread = None  # self.guests и self.thread

    def guest_arrival(self, *guests):
        self.guests = guests
        for g in self.guests:  # для каждого гостя
            if self.empty_tables > 0:  # пока есть пустые столы
                for i in range(self.table_amount):
                    if self.tables[i].guest is None:  # нашли пустой стол
                        self.tables[i].guest = g.name  # сажаем за него гостя
                        self.thread = Guest(g.name)  # присваиваем потоку имя гостя
                        self.thread.start()  # запускаем поток
                        self.threads.append(self.thread)  # добавляем поток в список потоков
                        print(f"{g.name} сел(-а) за стол номер {self.tables[i].number}")
                        self.empty_tables -= 1  # пустых столов стало меньше
                        break
            else:
                self.queue.put(g.name)  # остальных гостей в очередь
                print(f"{g.name} в очереди")

    def discuss_guests(self):
        while self.empty_tables != self.table_amount:  # пока есть занятые столы (и очередь не пуста -> это ниже)
            for i in range(self.table_amount):
                if self.tables[i].guest is not None:  # стол занят, проверяем поел ли гость
                    for th in self.threads:
                        if (th.name == self.tables[i].guest) and (not th.is_alive()):  # гость поел?
                            th.join()  # гость поел и ушел, поток закрываем
                            self.threads.remove(th)  # и удаляем его из списка потоков
                            print(f"{self.tables[i].guest} покушал(-а) и ушел(ла)")
                            self.tables[i].guest = None
                            self.empty_tables += 1  # пустых столов стало больше
                            print(f"Стол номер {self.tables[i].number} свободен")
                else:
                    if not self.queue.empty():  # пока очередь еще не пуста
                        self.tables[i].guest = self.queue.get()  # сажаем очередного гостя за стол
                        self.thread = Guest(self.tables[i].guest)  # присваиваем потоку имя гостя
                        self.thread.start()  # запускаем поток
                        self.empty_tables -= 1  # пустых столов стало меньше
                        self.threads.append(self.thread)  # добавляем поток в список потоков
                        print(f"{self.tables[i].guest} вышел(-ла) из очереди и "
                              f"сел(-а) за стол номер {self.tables[i].number}")


# Выполняемый код:
# =================

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# print([t.number for t in tables])

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests_ = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests_)

# Обслуживание гостей
cafe.discuss_guests()

# Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):
# ==============================================================================================

# Maria сел(-а) за стол номер 1
# Oleg сел(-а) за стол номер 2
# Vakhtang сел(-а) за стол номер 3
# Sergey сел(-а) за стол номер 4
# Darya сел(-а) за стол номер 5
# Arman в очереди
# Vitoria в очереди
# Nikita в очереди
# Galina в очереди
# Pavel в очереди
# Ilya в очереди
# Alexandra в очереди
# Oleg покушал(-а) и ушёл(ушла)
# Стол номер 2 свободен
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
# .....
# Alexandra покушал(-а) и ушёл(ушла)
# Стол номер 4 свободен
# Pavel покушал(-а) и ушёл(ушла)
# Стол номер 3 свободен
