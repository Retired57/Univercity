# Домашнее задание по теме "Файлы в операционной системе".

import os
import time

def get_folder_size(folder_path):                               # функция для подсчета объема папки =>
    total_size = 0                                              # => сумма размеров всех файлов
    for dirpath, dirnames, filenames in os.walk(folder_path):   # os.walk() - залезет во все уголки... )
        for f in filenames:
            file_path = os.path.join(dirpath, f)
            total_size += os.path.getsize(file_path)
    return total_size


def list_files_dirs(start_dir, files = True, dirs = False):     # основная функция - инфа по файлам и папкам
    if files:                                                   # секция файлов
        os.chdir(start_dir)
        start_dir=os.getcwd()
        print()
        print(f"Информация о файлах в директории {start_dir}")
        print()
        for dirpath, dirnames, filenames in os.walk(start_dir):
            b_in = False
            if len(filenames) > 0:
                if dirpath != start_dir:
                    os.chdir(dirpath)
                    b_in = True
                for file in filenames:
                    # parent_dir = os.path.dirname(os.path.abspath(file))
                    parent_dir = dirpath
                    filepath = os.path.join(parent_dir, file)
                    filesize = os.path.getsize(file)
                    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file)))
                    print(
                        f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
                        f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}'
                    )
                if b_in:
                    os.chdir("..")

    if dirs:                                                    # секция папок
        os.chdir(start_dir)
        print()
        print(f"Информация о папках в директории {start_dir}")
        print()
        for dirpath, dirnames, filenames in os.walk(start_dir):
            b_in = False
            if len(dirnames) > 0:
                if dirpath != start_dir:
                    os.chdir(dirpath)
                    b_in = True
                for folder in dirnames:
                    parent_dir = dirpath
                    dir_path = os.path.join(parent_dir, folder)
                    dirsize = get_folder_size(dir_path)
                    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(folder)))
                    print(
                        f'Обнаружена папка: {folder}, Путь: {dir_path}, Размер: {dirsize} байт, '
                        f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
                if b_in:
                    os.chdir("..")

directory = "."
list_files_dirs(directory,True, True)               # True - собираем инфу, False - нет


#=======================================================================================