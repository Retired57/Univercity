# Домашнее задание по уроку "Распаковка позиционных параметров".
# Задача "Распаковка"

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print()
print("Test 1")
print_params()
print_params(8)
print_params(8, 5)
print_params(8, 5, 13)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ["Hi", False, 3.14]
values_dict = {"a": True, "b": "Dmitry", "c": 1957}

print()
print("Test 2")
print_params(values_list)
print_params(*values_list)

print()
print("Test 3")
print_params(values_dict)
print_params(*values_dict)                  # только ключи
print_params(**values_dict)                 # только значения

print()
print("Test 4")
values_list_2 = [54.32, 'Строка' ]
print_params(values_list_2, 42)         # список в качестве 1-го аргумента
print_params(*values_list_2, 42)


