# Домашнее задание по теме "Декораторы"

def is_prime(in_func):
    def wrapper(*args):                     # так называемая "обертка"
        res = in_func(*args)
        if res > 1:                      # простое число должно быть больше 1
            for i in range(2, res):
                if not res % i:          # есть делители => составное
                    print("Составное")
                    return res
            print("Простое")                # делится только на себя => простое
            return res
        else:
            print("Сумма меньше 2")         # простое число должно быть больше 1
            return res
    return wrapper                          # возвращаем "обертку"

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример:
#========

result = sum_three(2, 3, 6)
print(result)


# Результат консоли:
#===================

# Простое
# 11
