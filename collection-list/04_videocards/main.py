N = int(input("Кол-во видеокарт: "))
old_list = []
new_list = []
max_num = 0
for i in range(1, N + 1):
    print(i, "Видеокарта:", end=" ")
    number = int(input())
    old_list.append(number)
    if number > max_num:
        max_num = number

for graphics_card in old_list:
    if graphics_card != max_num:
        new_list.append(graphics_card)
print("Старый список видеокарт: ", old_list)
print("Новый список видеокарт: ", new_list)

# зачёт!
