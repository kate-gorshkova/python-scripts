def synonym(my_dict):
    while True:
        word = input("Введите слово: ").title()
        if word in my_dict.keys():
            print("Синоним:", my_dict.get(word))
            break
        else:
            print("Такого слова в словаре нет.")


count_pair = int(input("Введите количество пар слов: "))
word_dict = dict()

for i_pair in range(1, count_pair + 1):
    print(i_pair, "пара:", end=" ")
    word_pair = input().title().split(" - ")
    word_dict[word_pair[0]] = word_pair[1]
    word_dict[word_pair[1]] = word_pair[0]

synonym(word_dict)

# зачёт!
