# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
# Задача "История строительства"
from operator import attrgetter


# Домашняя работа по уроку "Перегрузка операторов."
# Задача "Нужно больше этажей"

class House:

    __instanse = None
    def __new__(cls, *args, **kwargs):
        if cls.__instanse == None:
            cls.houses_history = []
            cls.__instanse = super().__new__(cls)
            cls.houses_history.append(args[0])
        else:
            cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name                                # название ЖК, которому принадлежит дом
        self.number_of_floors = number_of_floors        # кол-во этажей в доме
        # self.houses_history = name


    def __del__(self):
        print(f"{self.name} снесен, но он останется в истории.")


# Т Е С Т Ы
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)



"""
class Example:

    def __new__(cls, *args, **kwargs):
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")
        # print(f"kwargs = {kwargs[0]}")
        return super().__new__(cls)
        # return object.__new__(cls)

    def __init__(self, first, second, third):
        print(f"first = {first}")
        print(f"second = {second}")
        print(f"third = {third}")


     # def __init__(self, *args, **kwargs):
     #    print(f"args = {args}")
     #    print(f"kwargs = {kwargs}")

ex = Example('data', second=25, third=3.14)

"""