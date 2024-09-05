# Домашнее задание по теме "Множественное наследование"
# Задача "Мифическое наследование"

class Horse:

    def __init__(self, x_distance=0, sound='Frrr'):
        super().__init__()
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:

    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    sound = Eagle().sound

    def __init__(self):
        super().__init__()
        self.sound = Pegasus.sound

    def move(self, dx, dy):
        self.x_distance = super().run(dx)
        self.y_distance = super().fly(dy)

    def get_pos(self):
        coords = []
        coords.extend([self.x_distance, self.y_distance])
        return tuple(coords)

    def voice(self):
        print(self.sound)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Т Е С Т Ы
# Пример работы программы:
# =========================

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# Вывод на консоль:
# ==================

# (0, 0)
# (10, 15)
# (5, 35)
# I train, eat, sleep, and repeat
