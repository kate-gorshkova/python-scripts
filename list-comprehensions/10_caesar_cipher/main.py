message = input("Введите сообщение: ")
k = int(input("Введите сдвиг: "))
alphabet_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
new_message = [(" " if letter == " " else alphabet_letters[(alphabet_letters.index(letter) + k) % 33])
               for letter in message]
for letter in new_message:
    print(letter, end="")

# зачёт!
