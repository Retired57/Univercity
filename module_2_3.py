# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

positive_numbers = 0                # кол-во положительных чисел
i = 0                               # счетчик циклов

while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
        positive_numbers += 1
    elif my_list[i] < 0:
        break
    i += 1

print(f"Найдено {positive_numbers} положительных чисел.")

