def adding_contact(any_dict):
    surname_name = tuple(input("Введите фамилию и имя: ").title().split())
    phone_number = input("Введите номер телефона: ")
    if surname_name in any_dict:
        print("Ошибка: такое имя уже существует.")
    else:
        any_dict[surname_name] = phone_number
    print("\nТекущие контакты на телефоне:")
    for i_contact in any_dict:
        print("{n_s}: {telephone}".format(n_s=i_contact, telephone=any_dict[i_contact]))


def contact_search(any_dict):
    any_surname = input("Введите фамилию: ").title()
    for i_person, i_telephone in any_dict.items():
        if i_person[0] == any_surname:
            print(i_person, i_telephone)


contact_dict = dict()
print("Текущие контакты на телефоне:")
print("<Пусто>")
while True:
    action = input("\n«Добавить контакт» или «Поиск человека по фамилии»? ").title()
    if action == "Добавить Контакт":
        adding_contact(contact_dict)
    elif action == "Поиск Человека По Фамилии":
        contact_search(contact_dict)

# зачёт!
