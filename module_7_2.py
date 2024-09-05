# Домашнее задание по теме "Позиционирование в файле".
# Задача "Записать и запомнить"


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, "w", encoding = "utf-8")
    for i in range(len(strings)):
        dict_list1 = []
        dict_list2 = []
        cursor = file.tell()
        line = i + 1
        file.write(str(strings[i]) + "\n")              # запись строки в файл
        dict_list1.append(line)
        dict_list1.append(cursor)                       # формируем словарь так, чтобы вывод на консоль
        strings_positions[tuple(dict_list1)] = strings[i]
    file.close()
    return strings_positions


# Пример выполняемого кода:
#==========================

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
print()
for elem in result.items():
    print(elem)

# Вывод на консоль:
#===================

# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')

