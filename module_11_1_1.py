# Домашнее задание по теме "Обзор сторонних библиотек Python" (Часть 1)
# скачиваем изображения с сайта и работаем с ними

import requests
from PIL import Image, ImageOps

# Получаем текст HTML-страницы и скачиваем изображения !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# =====================================================
url = "https://instapik.ru/otkrytki/s-dnem-rozhdeniya/"
print("1. Скачиваем несколько первых изображений")
print(f"с сайта {url}")
print("и сохраняем их в виде Card_1.jpg .. Card_6.jpg")
response = requests.get(url)
txt_file = response.text  # необработанное содержание сайта в виде текстового файла

start, end, count, max_count = -1, 0, 1, 6
my_string, my_card = "", ""

while count <= max_count:  # ищем ссылки на рисунки в формате JPEG
    start = txt_file.find("http", start + 1)
    if start > 0:
        end = txt_file.find("http", start + 1)
    else:
        break
    if end <= 0:
        end = start + 1000
    end_jpg = txt_file.find(".jpg", start, end)
    if end_jpg > 0:
        my_string = txt_file[start:end_jpg + 4]  # нашли нужную строку
        if my_string.find("header") > 0:  # отбрасываем заголовки
            continue
        print(my_string)
        try:
            response = requests.get(my_string)  # выдергиваем изображение с сайта
        except:
            print("Что-то пошло не так с этим сайтом...")
            break
        if response.status_code == 200:
            my_card = f"Card_{count}.jpg"
            with open(my_card, "wb") as f:
                f.write(response.content)  # сохраняем изображение в рабочую папку
                count += 1
                im = Image.open(my_card)
                print(my_card, im.format, im.size, im.mode)

# меняем размер и формат изображений !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ==================================
print("2. Меняем размер всех изображений и их формат на PNG")
new_size = (1000, 800)  # новый размер
for i in range(1, max_count + 1):
    infile = f"Card_{i}.jpg"
    outfile = f"NewSize_{i}.png"
    try:
        with Image.open(infile) as im:
            ImageOps.fit(im, new_size).save(outfile)  # в точности по размеру
            im = Image.open(outfile)
            print(outfile, im.format, im.size, im.mode)
    except OSError:
        print(f"Изменить размер файла {infile} не удалось!")

# поворачиваем изображения !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# =========================
print(f"3. Поворачиваем изображения разные стороны")
for i in range(1, max_count + 1):
    infile = f"NewSize_{i}.png"
    outfile = f"Rotated_{i}.png"
    try:
        with Image.open(infile) as im:
            out = im.rotate(-45 * i)  # по часовой стрелке на 45 град * i
            out.save(outfile)
            print(outfile)
    except OSError:
        print(f"Поворот файла {infile} не удался!")

# вырезаем центр, разворачиваем его на 180 град, меняем цвет нв серый и вставляем обратно !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ==============================================================================
print("4. Вырезаем центр картинки, разворачиваем его на 180 град,")
print("изменяем его цвет на серый и вставляем обратно")
for i in range(1, max_count + 1):
    infile = f"NewSize_{i}.png"
    outfile = f"Center_{i}.png"
    try:
        with Image.open(infile) as im:
            x_segment = im.size[0] // 4
            y_segment = im.size[1] // 4
            box = (x_segment, y_segment, x_segment * 3, y_segment * 3)
            region = im.crop(box)
            region = region.transpose(Image.Transpose.ROTATE_180)
            region = region.convert("L")
            im.paste(region, box)
            im.save(outfile)
            print(outfile)
    except OSError:
        print(f"Фокус с файлом {infile} не удался!")

# теперь наоборот, вырезаем центр, разворачиваем его на 180 град, а цвет меняем самого изображения !!!!!!!!!!!!!!!!
# ================================================================================================
print("5. Теперь наоборот - меняем цвет рисунка,")
print("а вырез разворачиваем на 180 град и вставляем обратно")
for i in range(1, max_count + 1):
    infile = f"NewSize_{i}.png"
    outfile = f"Invert_{i}.png"
    try:
        with Image.open(infile) as im:
            x_segment = im.size[0] // 4
            y_segment = im.size[1] // 4
            box = (x_segment, y_segment, x_segment * 3, y_segment * 3)
            region = im.crop(box)
            region = region.transpose(Image.Transpose.ROTATE_180)
            region = region.convert("RGBA")
            im = im.convert("L")
            im = im.convert("RGBA")
            im.paste(region, box, mask=region)
            im.save(outfile)
            print(outfile)
    except OSError:
        print(f"Фокус с файлом {infile} не удался!")
