def input_field_count(string):
    return len(string.split()) == 3


def check_name(string):
    if string.isalpha():
        return True
    return False


def check_email(string):
    if "@" in string and "." in string:
        return True
    return False


def check_age(string):
    if string.isdigit() and 10 <= int(string) <= 99:
        return True
    return False


def total_check(string):
    if not input_field_count(string):
        raise ValueError("НЕ присутствуют все три поля")
    else:
        name, email, age = string.split()
        if not check_name(name):
            raise NameError("Поле имени содержит НЕ только буквы")
        elif not check_email(email):
            raise SyntaxError("Поле «Имейл» НЕ содержит @ и .(точку)")
        elif not check_age(age):
            raise ValueError("Поле «Возраст» НЕ является числом от 10 до 99")
        else:
            return string


with open("registrations.txt", "r") as registrations_file:
    for i_line in registrations_file:
        my_string = i_line
        try:
            if total_check(i_line):
                with open("registrations_good.log", "a") as good_file:
                    good_file.write(f"{my_string}")
        except (ValueError, NameError, SyntaxError):
            with open("registrations_bad.log", "a") as bad_file:
                bad_file.write(my_string)

# зачёт!
