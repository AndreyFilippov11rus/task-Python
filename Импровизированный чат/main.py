def choice():
    user = input('Введите никнейм: ')
    action = int(input('Выберите одно из действий:\n'
                    '1.Посмотреть текущий текст чата.\n'
                    '2.Отправить сообщение.\n'))
    if action == 1:
        open_chat()
    else:
        write_chat(user)


def open_chat():
    try:
        with open('chat.txt', 'r', encoding='utf-8') as chat:
            for line in chat:
                print(line)
    except:
        print('История сообщений пуста\n')
    finally:
        choice()


def write_chat(user):
    message = input('Введите сообщение:')
    with open('chat.txt', 'a', encoding='utf-8') as chat:
        chat.write(f'{user}: {message}\n')
    choice()


choice()





