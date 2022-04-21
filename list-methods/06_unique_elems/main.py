def my_list(stop, new_list):
    for i in range(1, stop):
        print("Введите", i, "число:", end=" ")
        num = int(input())
        new_list.append(num)


list1 = []
list2 = []
my_list(4, list1)
my_list(8, list2)
print("Первый список:", list1)
print("Второй список:", list2)
list1.extend(list2)
for number in list1:
    for _ in range(list1.count(number) - 1):
        list1.remove(number)
print("Новый первый список с уникальными элементами:", list1)

# зачёт!
