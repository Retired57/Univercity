#Домашняя работа по уроку "Атрибуты и методы объекта."
# Задача "Developer - не только разработчик"

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
                print(i)


# Т Е С Т Ы
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

