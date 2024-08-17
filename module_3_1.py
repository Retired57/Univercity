# Домашняя работа по уроку "Пространство имён"
# Задача "Счётчик вызовов"

calls = 0

def count_calls():                              # считает вызовы других функций
    global calls
    calls += 1


def string_info(string):                        # принимае строку. возвращает ее длину, верх. и нижн. регистры
    count_calls()
    return len(string), str.upper(string), str.lower(string)


def is_contains(string, list_to_search):        # принимаети строку, список и ищет в списке такую же строку
    count_calls()
    i = 0
    while i < len(list_to_search):
        if str.upper(list_to_search[i]) == str.upper(string):
            return True
        i += 1
    return False


def func1():                                    # организует работу STRING_INFO
    print()
    print("Функция STRING_INFO!")
    print()
    input_string = input("Введите строку: ")
    print()
    my_tuple = []                               # пока список
    my_tuple.extend(string_info(input_string))
    my_tuple = tuple(my_tuple)                  # теперь кортеж
    print(f"Ваш кортеж: {my_tuple}")
    print(f"Счетчик вызовов функций= {calls}")


def func2():                                    # организует работу IS_CONTAINS
    print()
    print("Функция IS_CONTAINS!")
    print()
    input_string = input("Введите строку: ")
    print()
    input_list = []
    while True:
        input_string2 = input("Окончание списка - пустая строка (Enter). Введите элемент списка: ")
        if input_string2 == "":
            break
        else:
            input_list.append(input_string2)
            print(f"Ваш текущий список: {input_list}")
    print()
    print(f"Ваш окончательный список: {input_list}")
    print()
    if is_contains(input_string, input_list):
        print(f"TRUE. Строка \'{input_string}\' ЕСТЬ в списке {input_list}")
    else:
        print(f"FALSE. Строки \'{input_string}\' НЕТ в списке {input_list}")
    print(f"Счетчик вызовов функций = {calls}")


# ЦЕНТР УПРАВЛЕНИЯ
while True:                                     # Организация работы всей программы
    print()
    print("НАЖМИТЕ  1 - функция STRING_INFO, 2 - функция IS_CONTATNS, 0 - завершение программы.")
    print()
    z = input("Ваш выбор: ")
    if (z != "1") and (z != "2") and (z != "0"):
        continue
    else:
        z = int (z)

    if z == 1:
        func1()                                 # STRING_INFO
    elif z == 2:
        func2()                                 # IS_CONTATNS
    elif z == 0:                                # выход из программы
        print()
        print("До новых встреч!")
        break


