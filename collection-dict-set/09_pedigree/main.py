def sort_dict(my_dict):
    sorted_dict = {key: my_dict[key] for key in sorted(my_dict.keys())}
    return sorted_dict


human_pair = int(input("Введите количество человек: "))
human_dict = dict()
height_dict = dict()

for i_pair in range(1, human_pair):
    print(i_pair, "пара:", end=" ")
    pair = input().split()
    human_dict[pair[0]] = pair[1]

for i_child in human_dict.keys():
    i_parent = human_dict.get(i_child)
    if i_parent not in human_dict.keys():
        height_dict[i_parent] = 0
        height_dict[i_child] = 1
    else:
        height_dict[i_child] = int(height_dict.get(i_parent)) + 1

sort_height_dict = sort_dict(height_dict)

print("\n“Высота” каждого члена семьи:")
for my_human in sort_height_dict.keys():
    print(my_human, sort_height_dict.get(my_human))

# зачёт!
