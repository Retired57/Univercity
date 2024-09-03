# Домашнее задание по теме "Генераторы"

def all_variants(text):
    for n in range(1, len(text) + 1):           # длина подстроки
        for k in range(len(text)):              # начальная позиция подстроки
            if k + n <= len(text):
                t = text[k : k + n]
                yield t


# Пример работы функции:
#=======================
#
a = all_variants("abc")
for i in a:
    print(i)

# Вывод на консоль:
#==================
# a
# b
# c
# ab
# bc
# abc

