import os


def save(any_text):
    while True:
        print("Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n")
        my_path_list = input().split()
        my_path = os.path.join(os.path.abspath(os.sep), *my_path_list)

        if os.path.exists(my_path):
            break
        else:
            print("Такого пути не существует. Введите последовательность папок ещё раз.\n")

    file_name = input("\nВведите имя файла: ") + ".txt"
    complete_name = os.path.join(my_path, file_name)
    if os.path.exists(complete_name):
        question = input("Вы действительно хотите перезаписать файл? ").lower()

        if question == "да":
            write(complete_name, any_text)

        read(complete_name)

    else:
        print("Файл успешно сохранён!")
        write(complete_name, any_text)
        read(complete_name)


def read(any_file_name):
    new_file_read = open(any_file_name, "r")
    print(new_file_read.read())
    new_file_read.close()


def write(any_file_name, some_text):
    new_file = open(any_file_name, "w")
    new_file.write(some_text)
    new_file.close()


text = input("Введите строку: ")
print()
save(text)

# зачёт!
