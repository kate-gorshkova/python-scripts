str_1 = input("Первая строка: ")
str_2 = input("Вторая строка: ")
str_1 = list(str_1)
str_2 = list(str_2)
for i in range(1, len(str_1) - 1):
    index = len(str_1) - 1
    last_element = str_1[index]
    while index > 0:
        str_1[index] = str_1[index - 1]
        index -= 1
    str_1[0] = last_element
    if str_1 == str_2:
        print("Первая строка получается из второй со сдвигом", i)
        break
if str_1 != str_2:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

# зачёт!
