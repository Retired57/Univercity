# Домашняя работа по уроку "Способы вызова функции"

def send_email(message, recipient, sender = "university.help@gmail.com"):
    print()
    if not (((str.endswith(recipient, ".com")) or                   # проверка окончаний .com .ru .net
        (str.endswith(recipient, ".net")) or
        (str.endswith(recipient, ".ru"))) and
        ((str.endswith(sender, ".com")) or
        (str.endswith(sender, ".net")) or
        (str.endswith(sender, ".ru"))) and
        (str.find(recipient,"@") > -1) and                          # проверка наличия символа @
        (str.find(sender,"@") > -1)):
        print(f"Невозможно отправить письмо с адреса \"{sender}\" на адрес \"{recipient}\"")

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса \"{sender}\" на адрес \"{recipient}\"")

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса \"{sender}\" на адрес \"{recipient}\"")


send_email("Это сообщение для проверки связи!", 'vasyok1337@gmail.com')

