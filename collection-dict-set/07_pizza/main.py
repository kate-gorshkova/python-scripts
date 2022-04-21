orders_count = int(input("Введите кол-во заказов: "))

orders_dict = dict()
for i_order in range(1, orders_count + 1):
    print(i_order, "заказ:", end=" ")
    order = input().split()
    surname, pizza, count = order
    pizza_dict = dict()
    if surname not in orders_dict:
        pizza_dict[pizza] = int(count)
        orders_dict[surname] = pizza_dict
    else:
        if pizza not in orders_dict.get(surname):
            pizza_dict = orders_dict.get(surname)
            pizza_dict[pizza] = int(count)
            orders_dict[surname] = pizza_dict
        else:
            pizza_dict = orders_dict.get(surname)
            pizza_dict[pizza] = int(pizza_dict.get(pizza)) + int(count)

print()

for j_name in orders_dict.keys():
    print(j_name + ":")
    for j_pizza in orders_dict.get(j_name):
        print("    " + j_pizza + ":", orders_dict[j_name][j_pizza])

# зачёт!
