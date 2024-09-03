# Домашнее задание по теме "Создание функций на лету"
# Задача "Функциональное разнообразие"

# 1) Lambda-функция:    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#================
print("1) Lambda-функция:")

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

# Результатом должен быть список совпадения букв в той же позиции:
#=================================================================

# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


# 2) Замыкание: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#==============
print()
print("2) Замыкание:")

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as my_file:     # создаем файл example.txt в текущей директории
            for el in data_set:
                el = str(el) + "\n"
                my_file.write(el)
        return file_name
    return write_everything


# Данный код:
#============

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print("Содержимое файла 'example.txt', который создан в текущей директории:")
with open('example.txt', "r", encoding="utf-8") as my_file:  # создаем файл example.txt в текущей директории
    txt = my_file.read()
print(txt)

# В файле example.txt записано:
#==============================
# Это строчка
# ['А', 'это', 'уже', 'число', 5, 'в', 'списке']


# 3) Метод __call__:  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#====================
print("3) Метод __call__:")

from random import choice

class MysticBall:

    def __init__(self,*words ):
        self.words = words

    def __call__(self):
        for i in range(len(self.words)):
            my_choice = choice(self.words)
            return my_choice


# Ваш код (количество слов для случайного выбора может быть другое):
#===================================================================
# Ваш класс здесь
#=================

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


# Примерный результат (может отличаться из-за случайности выбора):
#=================================================================
# Да
# Да
# Наверное

