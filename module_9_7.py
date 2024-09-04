# Домашнее задание по теме "Декораторы"

def is_prime(in_func):
    def out_func(*args):
        result = in_func(*args)
        if result > 1:                      # простое число должно быть больше 1
            for i in range(2, result):
                if not result % i:          # есть делители => составное
                    print("Составное")
                    return result
            print("Простое")                # делится только на себя => простое
            return result
        else:
            print("Сумма меньше 2")         # простое число должно быть больше 1
            return result
    return out_func

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
