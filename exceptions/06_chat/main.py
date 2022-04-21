name = input("Введите имя: ")
while True:
    print("1 - Посмотреть текущий текст чата; 2 - Отправить сообщение")
    try:
        operation = int(input())
        if operation == 1:
            try:
                with open("chat.txt", "r") as chat_file:
                    message = chat_file.readlines()
                    print("".join(message))
            except FileNotFoundError:
                print("Чат пуст.")
        elif operation == 2:
            new_message = input("Введите сообщение: ")
            with open("chat.txt", "a") as chat_file:
                chat_file.write("{}: {}\n".format(name, new_message))
        else:
            raise ValueError
    except ValueError:
        print("Пожалуйста введите 1 или 2.")

# зачёт!
