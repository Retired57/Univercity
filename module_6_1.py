# Домашнее задание по теме "Зачем нужно наследование"
# Задача "Съедобное, несъедобное"

# Ж И В О Т Н Ы Е
class Animal:

    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed


    def eat(self, food):
        if food.edible:
            self.fed = True             # сытый
            print(f"{self.name} съел {food.name}, сытый и живой")
        else:
            self.alive = False          # погиб
            print(f"{self.name} не стал есть {food.name}, погиб голодным")


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


# Р А С Т Е Н И Я
class Plant:

    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible


class Flower(Plant):
    pass


class Fruit(Plant):

    def __init__(self, name, edible=False):
        super().__init__(name)
        super().__init__(edible)
        self.name = name
        self.edible = True


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Выполняемый код(для проверки):
# ==============================

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

# Вывод на консоль:
# =================
#
# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True

