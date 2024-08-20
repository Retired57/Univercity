# Домашняя работа по уроку "Специальные методы классов"
# Задача "Магические здания"

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


# Т Е С Т Ы
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

