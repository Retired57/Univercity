# Домашнее задание по теме "Интроспекция"
import inspect


class my_class:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hello {self.name}")


# проверяем есть ли в нашем объекте встроенные классы, методы-обертки, функции и методы,
# а также какие атрибуты присущи этому объекту - это по умолчанию

def who_is(attr_name, attr_itself):
    if attr_name == "Class":  # есть ли встроенные классы в объекте
        if inspect.isclass(attr_itself):
            return True
    elif attr_name == "Methods Wrapper":  # есть ли встроенные методы-обертки
        if inspect.ismethodwrapper(attr_itself):
            return True
    elif attr_name == "Functions & Methods":  # есть ли встроенные функции и методы
        if inspect.isroutine(attr_itself):
            return True
    else:
        return False


def introspection_info(obj):
    # Список признаков, которые будем искать. Атрибуты - по умолчанию
    intro_names = ["Class", "Methods Wrapper", "Functions & Methods"]  # "Attributes" - по умолчанию
    result = {}  # итоговый словарь

    try:
        name = obj.__name__  # определяем имя объекта (если есть)
    except AttributeError:
        name = f"Объект '{obj}' не имеет имени."

    result["Object Name"] = name
    result["Module Name"] = __name__
    result["Type"] = type(obj)  # тип объекта

    obj_dir = dir(obj)

    new_attr = []
    rest_dir = []
    for intro in intro_names:  # классы, методы-обертки, функции и методы, атрибуты
        new_attr.clear()
        rest_dir.clear()
        for i in obj_dir:
            attr = getattr(obj, i)
            if who_is(intro, attr):
                new_attr.append(i)
            else:
                rest_dir.append(i)
        obj_dir.clear()
        obj_dir.extend(rest_dir)
        result[intro] = new_attr

    if len(rest_dir) > 0:
        result["Attributes"] = rest_dir  # все, что осталось - атрибуты

    return result


# Пример работы:
# ===============

number_info = introspection_info(my_class.say_hi)  # пример с функцией my_class.say_hi из моего класса
print(number_info)
number_info = introspection_info(my_class)  # пример с моим классом my_class
print(number_info)
number_info = introspection_info(["Это", "просто", "список"])  # пример со списком
print(number_info)
number_info = introspection_info(("А", "это", "кортеж"))  # пример с кортежем
print(number_info)
number_info = introspection_info("Просто строка")  # пример со строкой
print(number_info)
number_info = introspection_info(3.14)  # пример с дробным числом
print(number_info)

number_info = introspection_info(42)
print(number_info)

# Вывод на консоль:
# ==================

# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
