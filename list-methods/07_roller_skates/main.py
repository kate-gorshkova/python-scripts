N = int(input("Кол-во коньков: "))
skate_size = []
for i in range(1, N + 1):
    print("Размер", i, "пары:", end=" ")
    size_skate = int(input())
    skate_size.append(size_skate)

K = int(input("\nКол-во людей: "))
foot_size = []
for j in range(1, K + 1):
    print("Размер ноги", j, "человека:", end=" ")
    size_foot = int(input())
    foot_size.append(size_foot)

count = 0
for sizeFoot in foot_size:
    for sizeSkate in skate_size:
        if sizeSkate >= sizeFoot:
            count += 1
            skate_size.remove(sizeFoot)
            break
print("Наибольшее кол-во людей, которые могут взять ролики:", count)

# зачёт!
