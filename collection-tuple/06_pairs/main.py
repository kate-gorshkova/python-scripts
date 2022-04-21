import random

# Решение №1
origin_list = [random.randint(0, 9) for _ in range(10)]
print("Оригинальный список: {my_list}".format(my_list=origin_list))
new_list = [tuple([value, origin_list[index + 1]]) for index, value in enumerate(origin_list) if index % 2 == 0]
print("Новый список: {my_new_list}".format(my_new_list=new_list))

print()

# Решение №2
other_list = []
new_list = []
for index, value in enumerate(origin_list):
    if index % 2 == 0:
        other_list = []
        other_list.append(value)
    else:
        other_list.append(value)
        new_tuple = tuple(other_list)
        new_list.append(new_tuple)
print("Новый список: {my_new_list}".format(my_new_list=new_list))

print()

# Решение №3
flag = 0
new_list = []
my_list = []
for value in origin_list:
    if flag < 1:
        new_list.append(value)
        flag += 1
    elif flag == 1:
        new_list.append(value)
        new_list = tuple(new_list)
        my_list.append(new_list)
        new_list = []
        flag = 0
print("Новый список: {my_new_list}".format(my_new_list=my_list))

# зачёт!
