# Домашнее задание по теме "Многопроцессное программирование"
# Задача "Многопроцессное считывание"

from datetime import datetime
from multiprocessing import Pool


# Продолжительность линейного вызова: 0:00:06.935738
# Продолжительность многопроцессного вызова: 0:00:03.728149

def read_info(name):
    all_data = []
    with open(name, "r") as my_file:
        print(name)  # для контроля выполнения процесса
        while True:
            my_line = my_file.readline()
            if my_line == "":
                break
            else:
                all_data.append(my_line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# линейный вызов:
# ================
# start = datetime.now()
# for f_name in filenames:
#     read_info(f_name)
# end = datetime.now()
# print(f"Продолжительность линейного вызова: {end - start}")

# Многопроцессный:
# =================

if __name__ == '__main__':
    with Pool(processes=8) as my_pool:
        start = datetime.now()
        my_pool.map(read_info, filenames)
    end = datetime.now()
    print(f"Продолжительность многопроцессного вызова: {end - start}")

# Вывод на консоль, 2 запуска (результаты могут отличаться):
# ===========================================================

# 0:00:03.046163 (линейный)
# 0:00:01.092300 (многопроцессный)
