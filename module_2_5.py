# Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix(n, m, value):
    matrix = list()
    for i in range(n):
        matrix.append([])                       # создаем пустой список n раз
        for j in range(m):
            matrix[i].append(value)             # заполняем список значениями value в количестве m
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)

