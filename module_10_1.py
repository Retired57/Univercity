# Домашнее задание по теме "Создание потоков".
# Задача "Потоковая запись в файлы"

from datetime import datetime
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, "w", encoding="utf-8") as my_file:
        for i in range(1, word_count + 1):
            my_file.write(f"Какое-то слово № {i}" + "\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}.")

print("Обычные вычисления")
time_start = datetime.now()
# print(f"старт - {time_start}")

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end = datetime.now()
# print(f"финиш - {time_end}")

time_res1 = time_end - time_start
print(f"Работа одного потока - {time_res1}")

print()
print("Запись в файлы в 4-х потоках")

time_start = datetime.now()
# print(f"старт - {time_start}")

thr_first = Thread(target = write_words, args = (10, "example5.txt"))
thr_second = Thread(target = write_words, args = (30, "example6.txt"))
thr_third = Thread(target = write_words, args = (200, "example7.txt"))
thr_fourth = Thread(target = write_words, args = (100, "example8.txt"))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
# print(f"финиш - {time_end}")

time_res2 = time_end - time_start
print(f"Работа потоков - {time_res2}")

print()
print(f"С потоками быстрее в {round((time_res1 / time_res2), 2)} раза")


# Вывод на консоль:
#==================

# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время.
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время.
