N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", K, "человек")
my_list = list(range(1, N + 1))
additional_list = []
start = 0
for i in range(N - 1):
    print("\nТекущий круг людей:", my_list)
    print("Начало счёта с номера", my_list[start])
    drop_out_index = K % len(my_list) - 1 + start
    if my_list[drop_out_index] == my_list[-1]:
        start = 0
    else:
        start = drop_out_index
    drop_out = my_list[drop_out_index]
    my_list.remove(drop_out)
    print("Выбывает человек под номером", drop_out)
print("Остался человек под номером", my_list[0])

# зачёт!
