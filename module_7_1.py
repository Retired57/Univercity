# Домашнее задание по теме "Режимы открытия файлов"
# Задача "Учёт товаров"

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.my_file1 = ""
        file1 = open(self.__file_name, "r")
        self.my_file1 = file1.read()
        file1.close()
        return self.my_file1

    def add(self, *products):
        file2 = open(self.__file_name, "a")
        self.my_file = ""
        self.my_file = self.get_products()
        self.products = products
        for i in range(len(self.products)):
            self.find_string = self.products[i].name
            if self.my_file.upper().find(self.find_string.upper()) >= 0:
                print(f"Продукт {self.products[i]} уже есть в магазине.")
            else:
                file2.write(str(self.products[i]) + "\n")
        file2.close()


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Пример работы программы:
#==========================

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# p1 = Product('P', 5, 'V')
# p2 = Product('S', 3, 'G')
# p3 = Product('P', 5, 'V')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


# Вывод на консоль:
#===================

# Первый запуск:
#===============
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables

# Второй запуск:
#===============
# Spaghetti, 3.4, Groceries
# Продукт Potato, 50.5, Vegetables уже есть в магазине
# Продукт Spaghetti, 3.4, Groceries уже есть в магазине
# Продукт Potato, 5.5, Vegetables уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables

