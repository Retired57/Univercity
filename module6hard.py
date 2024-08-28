# Дополнительное практическое задание по модулю*
# Задание "Они все так похожи

class Figure:

    sides_count = 0                             # кол-во сторон фигуры
    PI = 3.14                                   # ПИ, оно и в Африке ПИ... )

    def __init__(self, color, *sides, filed = False):
        self.__color = color
        self.__sides = sides
        self.filed = filed

    def __str__(self):                          # это для самоконтроля, вывод инфы об объекте на консоль.
        return f"{type(self)}, color = {self.__color}, sides = {self.__sides}, filed = {self.filed}"

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):        # проверяем 0 <= r, g , b <= 255
        if ((0 <= r <= 255) and
            (0 <= g <= 255) and
            (0 <= b <= 255)):
            return True
        return False

    def set_color(self, r, g, b):              # если цвет соответствует условиям, меняем цвет
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):                        # получаем размер сторон фигуры
        return list(self.__sides)

    def __is_valid_sides(self, my_args):
        for i in range(len(my_args)):           # проверяет положительность всех длин сторон ( > 0 )
            if my_args[i] <= 0:
                return False
        if len(my_args) == 1:                   # если при этом всего 1 сторона, то подойдет для всех фигур
            return True
        if len(my_args) == self.sides_count:    # и проверяет строгое соответствие кол-ва переданных сторон
            if isinstance(self, Cube):          # для куба ввел доп проверку - все стороны куба должны быть одинаковыми
                return self.is_cube_sides(my_args)
            else:
                return True
        return False

    def set_sides(self, *new_sides):                # меняет размер фигуры, если длины и кол-во сторон соответствуют
        if self.__is_valid_sides(new_sides):
            if isinstance(self, Cube):              # для куба дополнительно проверяется равенство длин всех сторон
                if self.is_cube_sides(new_sides):
                    self.__sides = list(new_sides)
            else:
                self.__sides = list(new_sides)

    def __len__(self):                              # вычисляет периметр фигуры
        return sum(self.__sides)


class Circle(Figure):

    def __init__(self, color, *sides, filed = False):
        self.sides_count = 1
        self.__sides = sides
        if len(self.__sides) != self.sides_count:                       # если сторон больше, всем присваивается 1
            self.__sides = [1]
        super().__init__(color, *self.__sides, filed = False)
        self.__radius = self.__sides[0] / (2 * self.PI)                 # радиус окружности

    def get_square(self):
        return self.PI * (self.__radius ** 2)                           # площадь круга = пи * р в квадрате


class Triangle(Figure):

    def __init__(self, color, *sides, filed = False):
        self.sides_count = 3
        self.__sides = sides
        if len(self.__sides) == 1:                                  # если значение одно, то всем присваивается
            self.__sides = [self.__sides[0]] * self.sides_count     # длина первой стороны
        elif len(self.__sides) != self.sides_count:                 # если сторон меньше/больше, всем присваивается 1
            self.__sides = [1] * self.sides_count
        super().__init__(color, *self.__sides, filed = False)

    def get_square(self):                               # площадь треугольника по формуле Герона
        half_p = (self.__len__()) / 2
        sq = half_p
        for i in range(self.sides_count):
            sq *= (half_p - self.__sides[i])
        if sq < 0:
            sq = -sq
        return sq ** 0.5


class Cube(Figure):

    def __init__(self, color, *sides, filed = False):
        self.sides_count = 12
        self.__sides = sides
        if len(self.__sides) == 1:                                  # если значение одно, то всем присваивается
            self.__sides = [self.__sides[0]] * self.sides_count     # длина первой стороны
        elif len(self.__sides) != self.sides_count:                 # если сторон меньше/больше, всем присваивается 1
            self.__sides = [1] * self.sides_count
        else:                                                       # если сторон 12, то вынужден проверить
            if not self.is_cube_sides(self.__sides):                # равенство их длин. если не равны между собой =>
                self.__sides = [1] * self.sides_count               # => всем присваивается 1
        super().__init__(color, *self.__sides, filed = False)

    def is_cube_sides(self, cube_sides):            #  для куба дополнительно проверяется равенство длин всех сторон
        for i in range(1, len(cube_sides)):
            if cube_sides[i] != cube_sides[0]:
                return False
        return True

    def get_volume(self):                                               # объем куба = сторона в кубе... )
        return self.__sides[0] ** 3


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Т Е С Т Ы
# Код для проверки:
#==================

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# Выходные данные (консоль):
#===========================
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
