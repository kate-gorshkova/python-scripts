K = int(input("Сдвиг: "))
N = int(input("Введите число элементов списка: "))
initial_list = []
for element in range(N):
    list_element = int(input("Введите элемент списка: "))
    initial_list.append(list_element)
print("Изначальный список:", initial_list)

for _ in range(K):
    index = N - 1
    last_element = initial_list[index]
    while index > 0:
        initial_list[index] = initial_list[index - 1]
        index -= 1
    initial_list[0] = last_element
print(initial_list)

# зачёт!
