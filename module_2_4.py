# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

# Программа написана для поиска простых чисел в произвольном списке, а не только в "numbers"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

max_number = max(numbers) + 1                           # определяем верхний предел для делителей
print(f"Верхний предел для делителей = {max_number}")

for i in numbers:
    if i > 1:
        for j in range(2,max_number):                   # диапазон делителей range(2,max_number)
            if i == j:                                  # если число делится только на само себя, то число простое
                primes.append(i)
                break
            elif i % j == 0:                            # есть иные делители = признак составного числа
                not_primes.append(i)
                break

print(f"Исходных чисел {len(numbers)} = {numbers}")
print(f"Простых чмсел {len(primes)} = {primes}")
print(f"Составных чисел {len(not_primes)} = {not_primes}")

