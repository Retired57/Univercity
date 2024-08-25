# Дополнительное практическое задание по модулю 5* "Классы и объекты."
# Задание "Свой YouTube"

import time                                         # нужен секундомер для имитации секундного интервала видео

class User:                                         # класс пользователей (БД )

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:                                        # класс видео (БД фильмов)

    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []                             # создаем пустой список для БД ПОЛЬЗОВАТЕЛЕЙ
        self.videos = []                            # создаем пустой список для БД видео
        self.current_user = None                    # обнуляем атрибут текущего пользователя


    def log_in(self, nickname, password):           # вход в аккаунт, если имя и пароль совпали
        for i in range(len(self.users)):
            if (((nickname == self.users[i].nickname) and
                (hash(password) == self.users[i].password))):
                self.current_user = nickname        # после входа, клиент становится текущим пользователем
                break


    def register(self, nickname, password, age):
        not_found = True
        for i in range(len(self.users)):
            if nickname == self.users[i].nickname:          # имя совпало с БД
                print(f"Пользователь {nickname} уже существует!")
                not_found = False
                self.log_in(nickname, password)             # если имя и пароль совпадут => вход в аккаунт
                break
        if not_found:                                       # имени нет в БД => регистрация нового пользователя
            user = User(nickname, hash(password), age)
            self.users.append(user)
            self.current_user = nickname            # вновь зарегиный автоматически становится текущим current_user


    def log_out(self):                  # обнуляем текущего пользователя self.current_user
        self.current_user = None        # ему будет присвоено имя пользователя при регистрации или при входе в аккаунт


    def is_video(self, new_video):                  # проверяем, есть такое видео в нашей БД
        for i in range(len(self.videos)):           # этот метод используется в методе add()
            if new_video == self.videos[i].title:
                return True
        return False


    def add(self, *args):                           # ur.add(v1, v2, ...)
        for i in range(len(args)):                  # добавляем неограниченное количество фильмов класса Video
            if isinstance(args[i], Video):          # проверяем - тот ли класс аргумента? нужен только класс Video
                if not self.is_video(args[i].title):
                    self.videos.append(args[i])
            else:                                   # если класс аргумента не совпал с Video, не вносим в БД фильмов
                print(f"Не вношу в БД \"{args[i]}\". Запись о фильме оформлена неправильно!")


    def get_videos(self, find_string):              # формируем список фильмов из нашей БД с ключевым словом
        my_list = []
        for i in range(len(self.videos)):
            if find_string.upper() in self.videos[i].title.upper():
                my_list.append(self.videos[i].title)
        return my_list


    def is_adult(self, my_user):                            # проверка на зрелость >= 18 лет
        for i in range(len(self.users)):
            if (my_user == self.users[i].nickname) and (self.users[i].age >= 18):
                return True
        return False


    def watch_video(self, film_name):
        if not self.current_user:                                   # никто не вошел в аккаунт
            print("Войдите в аккаунт, чтобы смотреть видео.")
        else:
            for i in range(len(self.videos)):
                if film_name == self.videos[i].title:
                    if self.videos[i].adult_mode and not self.is_adult(self.current_user):      # фильм для взрослых
                        print("Вам нет 18 лет, пожалуйста покиньте страницу.")      # а клиент - малолетка
                        self.log_out()                                              # обнуляем текущего пользователя
                    else:
                        start_sec = self.videos[i].time_now + 1             # запускаем фильм с точки прошлой остановки
                        if (((self.videos[i].time_now <= 0) or
                            (self.videos[i].time_now >= self.videos[i].duration))):
                            start_sec = 1                           # с какой сек будем смотреть видео
                        for j in range(start_sec, self.videos[i].duration + 1):
                            print(j, end = " ")
                            self.videos[i].time_now = j             # записываем секунду возможной остановки просмотра
                            time.sleep(1)                           # имитация секундного интервала видео
                        print("Конец видео")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Т Е С Т Ы
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


# ВЫВОД НА КОНСОЛЬ

# ['Лучший язык программирования 2024 года']
# ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
# Войдите в аккаунт, чтобы смотреть видео
# Вам нет 18 лет, пожалуйста покиньте страницу
# 1 2 3 4 5 6 7 8 9 10 Конец видео
# Пользователь vasya_pupkin уже существует
# urban_pythonist
