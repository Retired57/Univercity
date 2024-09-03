# Домашнее задание по теме "Введение в функциональное программирование"
# Задача "Вызов разом"

def min(my_list):
    min_value = my_list[0]
    for val in my_list:             # перебираем список, сохраняем наименьшее значение
        if val < min_value:
            min_value = val
    return min_value


def max(my_list):
    max_value = my_list[0]
    for val in my_list:             # перебираем список, сохраняем наибольшее значение
        if val > max_value:
            max_value = val
    return max_value


def len(my_list):
    my_count = 0
    for val in my_list:             # перебираем список, считаем элементы списка
        my_count += 1
    return my_count


def sum(my_list):
    my_sumax = 0
    for val in my_list:             # перебираем список, складываем элементы списка
        my_sumax += val
    return my_sumax


def sorted(my_list):
    ls = []
    ls.extend(my_list)
    ls.sort()
    return ls


def apply_all_func(int_list, *functions):
    results = []
    for f in functions:                                 # перебираем функции
        list1 = []
        list1.append(f.__name__)                        # сначала делаем заготовку для словаря - список
        list1.append(f(int_list))
        results.append(list1)
    return dict(results)                                # возвращаем словарь


# Пример работы кода:
#====================

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


# Вывод на консоль:
#==================

#{'max': 20, 'min': 6}
# {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}


