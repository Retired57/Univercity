# Домашняя работа по уроку "Перегрузка операторов."
# Задача "Нужно больше этажей"

class House:

    def __init__(self, name, number_of_floors):
        self.name = name                                # название ЖК, которому принадлежит дом
        self.number_of_floors = number_of_floors        # кол-во этажей в доме


    def go_to(self, new_floor ):                        # метод "лифт"
        self.new_floor = new_floor

        if self.new_floor <= 1:                         # несуществующий для лифта этаж
            print("Вы ошиблись этажом!")
        elif self.new_floor > self.number_of_floors:    # номер этажа больше кол-ва этажей
            print("Такого этажа не существует!")
        else:
            for i in range(1, self.new_floor + 1):
                print(f"Этаж {i}")
            print("Приехали!")

# Магические методы (__len__ , __str__)
    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}."


    def __eq__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors == other.number_of_floors
        else:
            return "Несовместимые типы объектов!"


    def __ne__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors != other.number_of_floors
        else:
            return "Несовместимые типы объектов!"


    def __lt__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors < other.number_of_floors
        else:
            return "Несовместимые типы объектов!"


    def __le__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors <= other.number_of_floors
        else:
            return "Несовместимые типы объектов!"


    def __gt__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors > other.number_of_floors
        else:
            return "Несовместимые типы объектов!"


    def __ge__(self, other):
        if isinstance(other, House) :
            return self.number_of_floors >= other.number_of_floors
        else:
            return "Несовместимые типы объектов!"


    def __add__(self, value):
        if isinstance(self, House) and isinstance(value, int) :
            # self.number_of_floors = self.number_of_floors + value
            self.number_of_floors += value
            return self
        else:
            print("Несовместимые типы объектов!")
            return self


    def __radd__(self, value):
        if isinstance(self, House) and isinstance(value, int) :
            self.number_of_floors = value + self.number_of_floors
            return self
        else:
            print("Несовместимые типы объектов!")
            return self


    def __iadd__(self, value):
        if isinstance(self, House) and isinstance(value, int) :
            self.number_of_floors += value
            return self
        else:
            print("Несовместимые типы объектов!")
            return self


# Т Е С Т Ы
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__


