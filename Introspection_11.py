# Домашнее задание по теме "Интроспекция"
import inspect


class My_class:
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

number_info = introspection_info(My_class.say_hi)  # пример с функцией my_class.say_hi из моего класса
print(number_info)
number_info = introspection_info(My_class)  # пример с моим классом my_class
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

# {'Object Name': 'say_hi', 'Module Name': '__main__', 'Type': <class 'function'>, 'Class': ['__dir__', '__format__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__'], 'Methods Wrapper': ['__dir__', '__format__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__'], 'Functions & Methods': ['__dir__', '__format__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__'], 'Attributes': ['__annotations__', '__builtins__', '__closure__', '__code__', '__defaults__', '__dict__', '__doc__', '__globals__', '__kwdefaults__', '__module__', '__name__', '__qualname__', '__type_params__']}
# {'Object Name': 'My_class', 'Module Name': '__main__', 'Type': <class 'type'>, 'Class': ['__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'say_hi'], 'Methods Wrapper': ['__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'say_hi'], 'Functions & Methods': ['__delattr__', '__dir__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'say_hi'], 'Attributes': ['__dict__', '__doc__', '__module__', '__weakref__']}
# {'Object Name': "Объект '['Это', 'просто', 'список']' не имеет имени.", 'Module Name': '__main__', 'Type': <class 'list'>, 'Class': ['__class_getitem__', '__dir__', '__format__', '__getitem__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__reversed__', '__sizeof__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'], 'Methods Wrapper': ['__class_getitem__', '__dir__', '__format__', '__getitem__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__reversed__', '__sizeof__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'], 'Functions & Methods': ['__class_getitem__', '__dir__', '__format__', '__getitem__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__reversed__', '__sizeof__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'], 'Attributes': ['__doc__', '__hash__']}
# {'Object Name': "Объект '('А', 'это', 'кортеж')' не имеет имени.", 'Module Name': '__main__', 'Type': <class 'tuple'>, 'Class': ['__class_getitem__', '__dir__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__', 'count', 'index'], 'Methods Wrapper': ['__class_getitem__', '__dir__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__', 'count', 'index'], 'Functions & Methods': ['__class_getitem__', '__dir__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__', 'count', 'index'], 'Attributes': ['__doc__']}
# {'Object Name': "Объект 'Просто строка' не имеет имени.", 'Module Name': '__main__', 'Type': <class 'str'>, 'Class': ['__dir__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'], 'Methods Wrapper': ['__dir__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'], 'Functions & Methods': ['__dir__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__sizeof__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'], 'Attributes': ['__doc__']}
# {'Object Name': "Объект '3.14' не имеет имени.", 'Module Name': '__main__', 'Type': <class 'float'>, 'Class': ['__ceil__', '__dir__', '__floor__', '__format__', '__getformat__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__round__', '__sizeof__', '__subclasshook__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'is_integer'], 'Methods Wrapper': ['__ceil__', '__dir__', '__floor__', '__format__', '__getformat__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__round__', '__sizeof__', '__subclasshook__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'is_integer'], 'Functions & Methods': ['__ceil__', '__dir__', '__floor__', '__format__', '__getformat__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__round__', '__sizeof__', '__subclasshook__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'is_integer'], 'Attributes': ['__doc__', 'imag', 'real']}
# {'Object Name': "Объект '42' не имеет имени.", 'Module Name': '__main__', 'Type': <class 'int'>, 'Class': ['__ceil__', '__dir__', '__floor__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__round__', '__sizeof__', '__subclasshook__', '__trunc__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'from_bytes', 'is_integer', 'to_bytes'], 'Methods Wrapper': ['__ceil__', '__dir__', '__floor__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__round__', '__sizeof__', '__subclasshook__', '__trunc__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'from_bytes', 'is_integer', 'to_bytes'], 'Functions & Methods': ['__ceil__', '__dir__', '__floor__', '__format__', '__getnewargs__', '__getstate__', '__init_subclass__', '__new__', '__reduce__', '__reduce_ex__', '__round__', '__sizeof__', '__subclasshook__', '__trunc__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'from_bytes', 'is_integer', 'to_bytes'], 'Attributes': ['__doc__', 'denominator', 'imag', 'numerator', 'real']}


# атрибуты функции My_class.say_hi из моего класса =  ['__annotations__', '__builtins__', '__closure__', '__code__', '__defaults__', '__dict__', '__doc__', '__globals__', '__kwdefaults__', '__module__', '__name__', '__qualname__', '__type_params__']
# атрибуты моего класса My_class =  ['__dict__', '__doc__', '__module__', '__weakref__']
# атрибуты списка =  ['__doc__', '__hash__']
# атрибуты кортежа =  ['__doc__']
# атрибуты строки =  ['__doc__']
# атрибуты дробного числа =  ['__doc__', 'imag', 'real']
# атрибуты целого числа =  ['__doc__', 'denominator', 'imag', 'numerator', 'real']

