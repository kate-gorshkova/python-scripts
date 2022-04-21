list1 = [1, 5, 3]
list2 = [1, 5, 1, 5]
list3 = [1, 3, 1, 5, 3, 3]
list1.extend(list2)
count_five = list1.count(5)
print("Кол-во цифр 5 при первом объединении:", count_five)
for elem in list1:
    if elem == 5:
        list1.remove(elem)
list1.extend(list3)
count_three = list1.count(3)
print("Кол-во цифр 3 при втором объединении:", count_three)
print("Итоговый список:", list1)

# зачёт!
