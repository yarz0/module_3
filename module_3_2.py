def send_email(message='', recepient='', sender="university.help@gmail.com"):
    email = recepient
    email_1 = sender
    messages = []
    if recepient == sender:
        massages = None
        messages.append("Нельзя отправлять письмо самому себе")
    elif sender != "university.help@gmail.com":
        massages = None
        messages.append(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! письмо отправлено с адреса {sender} на адрес {recepient}")
    elif "@" in email:
        if email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"):
            if email_1.endswith(".com") or email_1.endswith(".ru") or email_1.endswith:
                massages = None
                messages.append(f"Письмо отправлено с адреса {recepient} на адрес {sender}")
        else:
            massages = None
            messages.append("Некорректный адрес отправителя или получателя")
    elif recepient == sender:
        massages = None
        messages.append("Нельзя отправлять письмо самому себе")
    return messages


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
