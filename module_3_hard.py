# Дополнительное практическое задание по модулю*
# Задание "Раз, два, три, четыре, пять .... Это не всё?"

sum_digits_lens = 0                                     # здесь суммируются числа и длины строк
recursion_counter = 0                                   # счетчик рекурсий


def calculate_structure_sum(*arg):
    global sum_digits_lens
    global recursion_counter

    recursion_counter += 1

    if isinstance(arg[0], list) or isinstance(arg[0], tuple) or isinstance(arg[0], set):
        my_list = list(arg[0])                          # для удобства все типы структур переводим в списки
    elif isinstance(arg[0], dict):
        my_list = list(arg[0].keys())
        my_list.extend(list(arg[0].values()))

    for i in my_list:
        if isinstance(i, int):                          # числа суммируем
            sum_digits_lens += i
#            print(sum_digits_lens)
        elif isinstance(i, str):                        # суммируем длины строк
            sum_digits_lens += len(i)
#            print(sum_digits_lens)
        else:
            calculate_structure_sum(i)                  # если опять попалась некая структура - РЕКУРСИЯ
    return sum_digits_lens


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print()
print(f"Сумма чисел и длин строк = {result}")
print()
print(f"количество рекурсий = {recursion_counter}")

