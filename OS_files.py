# Домашнее задание по теме "Файлы в операционной системе".

import os
import time

#   И З   Л Е К Ц И И
#======================

print(os.getcwd())
print(os.getlogin())

if os.path.exists("root13"):
    os.chdir("root13")
    print("Зашли!")
    print(os.getcwd())
else:
    os.mkdir("root13")
    print("Создали!")

os.makedirs(r"First\Second\Third")
print(os.getcwd())

print(os.listdir())

os.chdir(r"C:\Users\User\PycharmProjects\pythonProject2\Module 07")
print(os.getcwd())

for i in os.walk("."):
    print(i)

print("Files :")
files = [f for f in os.listdir() if os.path.isfile(f)]
print(files)
print("Dirs :")
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)

os.startfile(files[6])              # открывает файл 'Rudyard Kipling - If.txt'
print(os.stat(files[6]))            # статистика по этому файлу


#   И З   Д О М А Ш К И
#=======================

print(os.path.join(r"C:\Users\User\PycharmProjects\pythonProject2\Module 07\products.txt"))
print(os.path.dirname(r"C:\Users\User\PycharmProjects\pythonProject2\Module 07\products.txt"))

print(os.path.getsize(r"C:\Users\User\PycharmProjects\pythonProject2\Module 07\products.txt"))

# время не отформатировано = секунды с 1970 года
print(os.path.getmtime(r"C:\Users\User\PycharmProjects\pythonProject2\Module 07\products.txt"))
# время отформатировано в формате ДД/ММ/ГГГГ ЧЧ:ММ
print(time.strftime('%d/%m/%Y %H:%M', time.gmtime(os.path.getmtime(r"C:\Users\User\PycharmProjects\pythonProject2\Module 07\products.txt"))))

