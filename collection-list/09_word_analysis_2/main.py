s = input("Введите слово: ")
old_list = list(s)
new_list = []
i = -1
while len(s) >= abs(i):
    new_list.append(old_list[i])
    i -= 1
if old_list == new_list:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")

# зачёт!
