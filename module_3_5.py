# Самостоятельная работа по уроку "Рекурсия"
# Задача "Рекурсивное умножение цифр"

nb = 0

def get_multiplied_digits(number ):
    str_number = str(number)
    first = int(str_number[0])
    print(f" Длина = {len(str_number)}, first = {first}")
    if len(str_number) <= 1:
        return first
    return first * get_multiplied_digits(int(str_number[1:]))


# Т Е С Т
result = get_multiplied_digits(40203)
print()
print(f"Произведение значимых цифр числа = {result}")

