class1 = list(range(160, 177, 2))
class1.extend(range(162, 181, 3))
for i in range(len(class1) - 1):
    for j in range(len(class1) - i - 1):
        if class1[j] > class1[j + 1]:
            class1[j], class1[j + 1] = class1[j + 1], class1[j]
print("Отсортированный список роста учеников двух классов:", class1)

# зачёт!
