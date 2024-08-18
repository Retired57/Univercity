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


print()
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
