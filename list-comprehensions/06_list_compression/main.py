import random

N = int(input("Кол-во чисел в списке: "))
my_list = [random.randint(0, 5) for _ in range(N)]
print(my_list)
my_list1 = [num for num in my_list if num != 0] + [0] * my_list.count(0)
print(my_list1)
my_list1 = [num for num in my_list if num != 0]
print(my_list1)

# зачёт!
