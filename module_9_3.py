# Домашнее задание по теме "Генераторные сборки"
#

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(z[0]) - len(z[1]) for z in zip(first, second) if len(z[0]) != len(z[1]))
second_result = (True if len(first[i]) == len(second[i]) else False for i in range(len(first)))


# Пример выполнения кода:
#========================

print(list(first_result))
print(list(second_result))


# Вывод в консоль:
#=================

# [1, 2]
# [False, False, True]

