# Домашнее задание по теме "Обзор сторонних библиотек Python" (Часть 2)
# скачиваем архивные тиражи с сайта Русского лото и готовим данные для первичного анализа

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Номера Русского лото
# =====================

# Первая часть программы.
# Считываем с сайта нужную информацию и записываем ее в файл .CSV
# =================================================================

all_circulations = []  # данные по всем тиражам (общая БД)
all_numbers = []  # все не выпавшие числа во всех тиражах
max_non_fallen = 5  # макс число не выпавших в одном тираже чисел

tirs_file_name = "RusLoto.csv"
stat_file_name = "Stat_RusLoto.csv"

url = "https://www.stoloto.ru/ruslotto/archive"  # архив сайта Русского лото
response = requests.get(url)
txt_file = response.text  # необработанное содержание сайта в виде текстового файла

p1 = 0
while True:  # ищем и извлекаем нужную информацию
    tir_numbers = []  # номер одного тиража и не выпавшие в нем числа
    p1 = txt_file.find("/ruslotto/archive/", p1)
    if p1 > 0:
        tir = int(txt_file[p1 + 18: p1 + 22])  # номер тиража
        tir_numbers.append(tir)
        p1 += 30
        p3 = txt_file.find("</span>", p1)
        if p3 > 0:
            count = 0
            while True:
                p2 = txt_file.find("<b>", p1, p3)
                if p2 > 0:
                    num = int(txt_file[p2 + 3: p2 + 5])  # не выпавшее число
                    tir_numbers.append(num)
                    all_numbers.append(num)
                    count += 1
                    p1 = p2 + 8
                else:
                    break
            for i in range(count, max_non_fallen):  # нет чисел - дополняем строку таблицы нулями
                tir_numbers.append(0)
            all_circulations.append(tir_numbers)  # добавляем тираж в общую БД
        else:
            break
    else:
        break

df = pd.DataFrame(all_circulations, index=list(range(1, len(all_circulations) + 1)))  # формируем DateFrame
df.columns = "Тираж", "Число 1", "Число 2", "Число 3", "Число 4", "Число 5"

print()
print("Таблица чисел, не выпавших в тиражах.")
print(df)

try:
    df.to_csv(tirs_file_name, sep=";", encoding="cp1251")  # записываем DF в файл .CSV
except:
    print()
    print(f"Не могу записать данные! Закройте файл {tirs_file_name} !!!")

# Вторая часть программы.
# ===============================================================================================
# Теперь обнуляем список all_circulations со всем данными (наша БД), скачанными с сайта.
# и применяем метод READ - считываем данные из только что записанного на компе файла RusLoto.csv.

all_circulations.clear()  # стерли все данные, а затем читаем данные из файла RusLoto.csv
df = pd.read_csv("RusLoto.csv", sep=";", encoding="cp1251", usecols=[1, 2, 3, 4, 5, 6])
all_circulations = df.values.tolist()  # переводим DateFrame в простой список

# Третья часть программы.
# составляем частотную характеристику и записываем ее в новый файл Stat_RusLoto.csv
# =================================================================================

numbers = []
freq = [0] * 91

for i in range(len(all_circulations)):
    for j in range(1, max_non_fallen + 1):
        if all_circulations[i][j] != 0:
            freq[int(all_circulations[i][j])] += 1  # считаем, как часто не выпадали числа

for i in range(1, 91):
    ls = []
    ls.append(i)
    ls.append(freq[i])
    numbers.append(ls)  # заполняем таблицу

df_stat = pd.DataFrame(numbers, index=list(range(1, len(numbers) + 1)))  # преобразуем таблицу в DF
df_stat.columns = "Число", "Частота",

print()
print("Таблица частоты НЕвыпадения чисел в тиражах.")
print(df_stat)

try:
    df_stat.to_csv(stat_file_name, sep=";", encoding="cp1251")  # записываем данные в новый файл Stat_RusLoto
except:
    print()
    print(f"Не могу записать данные! Закройте файл {stat_file_name} !!!")

# рисуем график последней таблицы
# ================================
plt.plot(freq)
plt.title('Частота НЕвыпадения чисел (1..90) в тиражах Русского лото')
plt.xlabel('Числа')
plt.ylabel('Частота')
plt.grid(True)
plt.xlim(0, 90)
plt.ylim(0, 6)
plt.show()
