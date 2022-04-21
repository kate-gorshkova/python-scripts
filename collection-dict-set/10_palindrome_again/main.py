def check_palindrome(stroke):
    my_dict = dict()
    for i_letter in stroke:
        my_dict[i_letter] = my_dict.get(i_letter, 0) + 1

    num_count = 0
    for i_value in my_dict.values():
        if i_value % 2 != 0:
            num_count += 1

    return num_count <= 1


string = input("Введите строку: ")
if check_palindrome(string):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")

# зачёт!
