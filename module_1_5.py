# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_tiple = (5, 4.56, "Hello", True, [1,2,3])
print("Неизменяемый кортеж: ",immutable_tiple)

print("Третий элемент кортежа: ", immutable_tiple[2])
# immutable_tiple[2] = "Привет" - здесь выдал ошибку - кортеж не поддерживает такое присвоение значений
print("Изменить элемент кортежа не удалось...")
print("Третий элемент кортежа: ",immutable_tiple[2])

mutable_list = [5, 4.56, "Hello", True, [1,2,3]]
print("Изменяемый список: ", mutable_list)

print("Меняем все элементы списка...")
mutable_list[0] = 3.14
mutable_list[1] = 7
mutable_list[2] = "Привет"
mutable_list[3] = False
mutable_list.remove(mutable_list[4])
print("Измененный список: ", mutable_list)

mutable_list = mutable_list[::-1]
print("Измененный список наоборот: ", mutable_list)

