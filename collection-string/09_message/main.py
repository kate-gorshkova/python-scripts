message = input("Сообщение: ")
new_str = ""
my_str = ""
for letter in message:
    if letter.isalpha():
        my_str += letter
    else:
        new_str += my_str[::-1]
        new_str += letter
        my_str = ""
new_str += my_str[::-1]
print("Новое сообщение:", new_str)

# зачёт!
