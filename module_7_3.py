# Домашнее задание по теме "Оператор "with".
# Задача "Найдёт везде"

class WordsFinder:

    _points = [',', '.', '=', '!', '?', ';', ':', ' - ']            # заменяем эти символы пробелами

    def __init__(self, *args):
        self.args = args
        self.file_names = []
        self.word = ""
        for i in range(len(self.args)):
            self.file_names.append(args[i])

    def get_all_words(self):
        dict_list = []
        for i in self.file_names:                               # перебираем все файлы
            with open(i, "r", encoding="utf-8") as my_file:     # открываем файл
                file_ = my_file.read().lower()                  # считываем сразу в строчных буквах
            my_list = []
            file = ""
            for j in range(len(self._points)):                                  # перебираем запрещенные символы
                file = file_.replace(self._points[j], " ").split()        # заменяем пробелами и сплитуем
            my_list.append(i)
            my_list.append(file)
            dict_list.append(my_list)                       # формируем нужный список
        all_words = dict(dict_list)                         # и создаем словарь
        return all_words

    def find(self, word):
        self.word = word.lower()
        dict_list = []
        for i in self.file_names:                           # перебираем все файлы
            my_list = []
            list_i = self.get_all_words().get(i)            # использую метод get_all_words(self)
            pos = 0
            for j in range(len(list_i)):
                if list_i[j] == self.word:
                    pos = j + 1
                    break
            my_list.append(i)
            my_list.append(str(pos))
            dict_list.append(my_list)                       # формируем нужный список
        word_position = dict(dict_list)                     # и создаем словарь
        return word_position

    def count(self, word):
        self.word = word.lower()
        dict_list = []
        for i in self.file_names:                           # перебираем все файлы
            my_list = []
            list_i = self.get_all_words().get(i)            # использую метод get_all_words(self)
            count = 0
            for j in range(len(list_i)):
                if list_i[j] == self.word:
                    count += 1
            my_list.append(i)
            my_list.append(str(count))
            dict_list.append(my_list)                       # формируем нужный список
        word_count = dict(dict_list)                        # и создаем словарь
        return word_count


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Пример выполнения программы:
#=============================

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))


# Вывод на консоль:
#==================

# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}

