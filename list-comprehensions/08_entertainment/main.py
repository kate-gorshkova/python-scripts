import random

N = int(input("Кол-во палок: "))
K = int(input("Кол-во бросков: "))
part_1 = ""
part_2 = ""
part_3 = ""
total_res = "|" * N
res = ""
for throw in range(1, K + 1):
    print("Бросок", str(throw) + ".", end=" ")
    my_list = [random.randint(1, N) for _ in range(2)]
    min_num = min(my_list)
    max_num = max(my_list)
    print("Сбиты палки с номера", min_num)
    print("по номер", max_num)
    dot = (max_num - min_num + 1) * "."
    res = total_res[:min_num - 1] + dot + total_res[max_num:]
    total_res = res
print(res)

# зачёт!
