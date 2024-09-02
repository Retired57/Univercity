# Домашнее задание по теме "Создание исключений".
# Задача "Некорректность"

class IncorrectVinNumber(Exception):                # создаем класс своего исключения для VinNumber
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):               # создаем класс своего исключения для CarNumber
    def __init__(self, message):
        self.message = message


class Car:                                          # класс для регистрации машин
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):                # запускаем проверку VinNumber
            self.__vin = vin
        self.__numbers = numbers
        if self.__is_valid_numbers(numbers):        # запускаем проверку CarNumber
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")          # передаем в свой класс описание ошибки
        elif not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")    # передаем в свой класс описание ошибки
        return True

    def __is_valid_numbers(self, gov_number):
        if not isinstance(gov_number, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")    # передаем в свой класс описание ошибки
        elif len(gov_number) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")                  # передаем в свой класс описание ошибки
        return True


# Пример выполняемого кода:
#==========================

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


# Вывод на консоль:
#==================

# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера


