person_count = int(input("Сколько человек в базе данных? "))
data_base = dict()
for _ in range(person_count):
    surname_name = tuple(input("Введите фамилию и имя: ").title().split())
    year = input("Введите возраст: ")
    data_base[surname_name] = year

surname = input("Введите фамилию: ").title()
len_surname = len(surname)
for i_person, i_year in data_base.items():
    my_surname, my_name = i_person[0], i_person[1]
    len_my_surname = len(my_surname)

    if my_surname == surname or my_surname[:len_my_surname - 3] == surname[:len_surname - 2] \
            or my_surname[:len_my_surname - 2] == surname[:len_surname - 3]:
        print(my_surname, my_name, i_year)

# зачёт!
