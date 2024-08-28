# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = int(input("Введите первое целое число: "))
print("Первое число: ", first)

second = int(input("Введите второе целое число: "))
print("Второе число: ", second)

third = int(input("Введите третье целое число: "))
print("Третье число: ", third)

if (second == first) and (second == third):
    print(f"Вариант 3. Все числа равны между собой. {first} = {second} = {third}")
elif second == first:
    print(f"Вариант 2. Нашлась пара равных между собой чисел (1-е и 2-е). {first} = {second}")
elif second == third:
    print(f"Вариант 2. Нашлась пара равных между собой чисел (2-е и 3-е). {second} = {third}")
elif first == third:
    print(f"Вариант 2. Нашлась пара равных между собой чисел (1-е и 3-е). {first} = {third}")
else:
    print(f"Вариант 0. Нет равных между собой чисел. {first} <> {second} <> {third}")


# if (second == first) and (second == third):
#     print(f"Вариант 3. Все числа равны между собой. {first} = {second} = {third}")
# elif (first == second) or (second == third) or (first == third):
#     if second == first:
#         print(f"Вариант 2. Нашлась пара равных между собой чисел (1-е и 2-е). {first} = {second}")
#     elif second == third:
#         print(f"Вариант 2. Нашлась пара равных между собой чисел (2-е и 3-е). {second} = {third}")
#     else:
#         print(f"Вариант 2. Нашлась пара равных между собой чисел (1-е и 3-е). {first} = {third}")
# else:
#     print(f"Вариант 0. Нет равных между собой чисел. {first} <> {second} <> {third}")
