# Домашнее задание по теме "Оператор "with".
# Задача "Найдёт везде"

class WordsFinder:
    _points = [',', '.', '=', '!', '?', ';', ':', ' - ']  # заменяем эти символы пробелами

    def __init__(self, *args):
        self.args = args
        self.file_names = []
        self.word = ""
        # новый вариант
        for nf in self.args:
            self.file_names.append(nf)

    def get_all_words(self):
        all_words = {}
        for fn in self.file_names:  # перебираем все файлы
            with open(fn, "r", encoding="utf-8") as my_file:  # открываем файл
                text = my_file.read().lower()  # считываем сразу в строчных буквах

            file = ""
            for p in self._points:  # перебираем запрещенные символы
                file = text.replace(p, " ").split()  # заменяем пробелами и сплитуем
            all_words[fn] = file  # и создаем словарь
        return all_words

    def find(self, word):
        self.word = word.lower()
        word_position = {}
        for fn in self.file_names:  # перебираем все файлы
            list_i = self.get_all_words().get(fn)  # использую метод get_all_words(self)
            pos = 0
            for w in list_i:
                pos += 1
                if w == self.word:
                    break
            word_position[fn] = str(pos)  # и создаем словарь
        return word_position

    def count(self, word):
        word_count = {}
        self.word = word.lower()
        for fn in self.file_names:  # перебираем все файлы
            list_i = self.get_all_words().get(fn)  # использую метод get_all_words(self)
            count = 0
            for w in list_i:
                if w == self.word:
                    count += 1
            word_count[fn] = str(count)  # и создаем словарь
        return word_count


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Пример выполнения программы:
# =============================

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))


# Вывод на консоль:
# ==================

# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
