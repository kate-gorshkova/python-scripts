def check_containers_weight(weight):
    if weight <= 200:  # Можно сразу return weight <= 200.
        return True
    else:
        return False


containers_count = int(input("Кол-во контейнеров: "))
containers_list = []
final_list = []
count1 = 0
container_weight1 = 200
while containers_count > count1:
    container_weight = int(input("Введите вес контейнера: "))
    if check_containers_weight(container_weight) and container_weight <= container_weight1:
        count1 += 1
        containers_list.append(container_weight)
        container_weight1 = container_weight

X = int(input("\nВведите вес нового контейнера: "))
count2 = 0
while count2 == 0:
    if check_containers_weight(X):
        count2 += 1
    else:
        X = int(input("Введите вес нового контейнера: "))

for container in containers_list:
    if X <= container:
        final_list.append(container)
final_list.append(X)
print("\nНомер, куда встанет новый контейнер:", len(final_list))

# зачёт!
