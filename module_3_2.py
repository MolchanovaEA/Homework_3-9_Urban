def send_email(message, recipient, sender = "university.help@gmail.com"):
    words1 = '@'
    words2 = ['.com', '.ru', '.net']

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    else:
        if sender != "university.help@gmail.com":
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient)
        else:
            if words1 in recipient and sender:
                if any(word in recipient and sender for word in words2):
                    print('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
                else:
                    print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
            else:
                print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)

send_email('Здравствуйте! Неверное окончание адреса', 'qwe@.mail')
send_email('Здравствуйте! В адресе нет @', 'qwe.ru')
send_email('Здравствуйте! Отправитель и получатель совпадают', 'university.help@gmail.com')
send_email('Здравствуйте! Отправитель не по умолчанию', 'qwe@.com', sender = 'asd@.ru')
send_email('Здравствуйте! Все верно ', 'qwe@.com')

