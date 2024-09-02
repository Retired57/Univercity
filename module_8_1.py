# Домашнее задание по теме "Try и Except".
# Задание "Программистам всё можно"


def add_everything_up(a, b):
    c = 0
    try:
        c = a + b
    except TypeError:
        if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, str)):  # a - число, b - строка
            return str(a) + b
        elif (isinstance(b, int) or isinstance(b, float)) and (isinstance(a, str)):  # а - строка, b - число
            return a + str(b)

    if isinstance(c, str):
        return c                                        # сложили две строки
    else:
        return round(c, 3)                              # сложили два числа


# Пример кода:
#==============
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('яблоко', 'строка'))

# Вывод в консоль:
#=================
# 123.456строка
# яблоко4215
# 130.456
# яблокострока

