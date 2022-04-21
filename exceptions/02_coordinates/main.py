import random


def f(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y


def f2(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x


number = random.randint(0, 100)
my_list = list()
my_list.append(number)

with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()

        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print("На ноль делить нельзя (y = 0).")
            res1 = 0
        my_list.append(res1)
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            my_list.append(res2)
        except ZeroDivisionError:
            print("На ноль делить нельзя (x = 0).")
            res2 = 0
        my_list.append(res2)

        with open('result.txt', 'w') as file_2:
            sort_list = sorted(my_list)
            new_sort_list = []
            for i_sym in sort_list:
                i_sym = str(i_sym)
                new_sort_list.append(i_sym)
            string = " ".join(new_sort_list)
            file_2.write(''.join(string))

# зачёт!
