# Домашняя работа по уроку "Пространство имен."

# ГЛОБАЛЬНОЕ пространство
def test_function():
    # ЛОКАЛЬНОЕ пространство
    def  inner_function():
        print()
        print("Я в области видимости функции test_function")
    inner_function()


# вызов из ГЛОБАЛЬНОГО пространства функции, которая находится в там же
test_function()


# вызов из ГЛОБАЛЬНОГО пространства функции, которая находится ЛОКАЛЬНОМ пространстве
# inner_function()      # ОШИБКА! из глобального пространства имен не видно локального...
