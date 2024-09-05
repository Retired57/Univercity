# Домашнее задание по теме "Потоки на классах"
# Задача "За честь и отвагу!"

from threading import Thread
from time import sleep

enemy_number = 100


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = enemy_number
        self.day_count = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while True:
            if self.enemy > 0:
                sleep(1)
                self.day_count += 1
                self.enemy -= self.power
                print(f"{self.name} сражается {self.day_count}-й день, осталось {self.enemy} воинов.")
            else:
                print(f"{self.name} одержал победу спустя {self.day_count} дней(дня)!")
                break

# Алгоритм выполнения кода:
# ==========================

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()                                    # запускаем поток 1
second_knight.start()                                   # запускаем поток 2

first_knight.join()                                     # завершаем поток 1
second_knight.join()                                    # завершаем поток 2

print("Все битвы закончились!")

# Вывод на консоль:
# ==================

# Sir Lancelot, на нас напали!
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
# Sir Galahad, на нас напали!
# Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.
# Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
# Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
# Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.
# Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
# Sir Galahad одержал победу спустя 5 дней(дня)!
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
# Sir Lancelot одержал победу спустя 10 дней(дня)!
# Все битвы закончились!
