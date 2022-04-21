shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
part_name = input("Название детали: ")
count = 0
total_sum = 0
for part in shop:
    name = part[0]
    if name == part_name:
        total_sum += part[1]
        count += 1
print("Кол-во деталей -", count)
print("Общая стоимость -", total_sum)

# зачёт!
