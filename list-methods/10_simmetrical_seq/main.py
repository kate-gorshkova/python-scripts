N = int(input("Кол-во чисел: "))
my_list = []
done_list = []
done_rev = ""
my_list_str = ""
for _ in range(N):
    num = int(input("Число: "))
    my_list.append(num)
    my_list_str += str(num) + " "
print("\nПоследовательность:", my_list_str)

for _ in range(len(my_list)):
    new_list = []
    for i in range(len(my_list), 0, -1):
        new_list.append(my_list[i - 1])
    if new_list != my_list:
        done_list.append(my_list[0])
        my_list.remove(my_list[0])

print("Нужно приписать чисел:", len(done_list))

for number in range(len(done_list), 0, -1):
    done_rev += str((done_list[number - 1])) + " "
print("Сами числа:", done_rev)

# зачёт!
