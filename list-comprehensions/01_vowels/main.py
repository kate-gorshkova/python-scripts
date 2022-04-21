text = input("Введите текст: ")
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
vowels_list = [letter for letter in text if letter in vowels]
print("Список гласных букв:", vowels_list)
print("Длина списка:", len(vowels_list))

# зачёт!
