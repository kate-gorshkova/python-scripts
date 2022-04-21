def check_letter(my_password):
    for my_letter in my_password:
        if my_letter.isupper():
            return True
    return False


def check_number_count(my_password):
    num_count = 0
    for sym in my_password:
        if sym.isdigit():
            num_count += 1
            if num_count == 3:
                return True
    return False


while True:
    password = input("Придумайте пароль: ")
    if len(password) >= 8 and password.isalnum() and check_letter(password) and check_number_count(password):
        print("Это надёжный пароль!")
        break
    print("Пароль ненадёжный. Попробуйте ещё раз.")

# зачёт!
