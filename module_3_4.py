# Самостоятельная работа по уроку "Произвольное число параметров".
# Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if ((str.find(str.upper(root_word), str.upper(other_words[i])) > -1) or
            (str.find(str.upper(other_words[i]), str.upper(root_word)) > -1)):
            same_words.append(other_words[i])
    return same_words


# Т Е С ТЫ
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print()
print(result1)
print(result2)

