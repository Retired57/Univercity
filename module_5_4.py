# Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
# Задача "История строительства"


class House:

    __instanse = True                               # переменная обеспечивает однократное формирование пустого списка

    def __new__(cls, *args, **kwargs):
        if cls.__instanse:
            cls.houses_history = []                 # создаем пустой список, но только 1 раз при создании 1-го объекта
            cls.__instanse = False

        cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name                                # название ЖК, которому принадлежит дом
        self.number_of_floors = number_of_floors        # кол-во этажей в доме


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
print()
print("Конец программы")        # по завершению проги деструктор ложно сообщит о сненсении последнего ЖК - "Эльбрус"
print()


