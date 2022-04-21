first_tour = open("first_tour.txt", "r")

person_count = 0
player_dict = dict()

for i_line in first_tour.readlines()[1:]:
    person_count += 1
    player = i_line.split()
    player_dict[tuple(player[0:2])] = player[2]
first_tour.close()

first_tour = open("first_tour.txt", "r")
K = int(first_tour.readlines()[0])

first_tour.close()

sorted_tuples = sorted(player_dict.items(), key=lambda item: item[1], reverse=True)

count_player = 0
new_dict = dict()
for i_player in sorted_tuples:
    if int(i_player[1]) > K:
        count_player += 1
        new_dict[i_player[0][1][0] + ".", i_player[0][0]] = i_player[1]

second_tour = open("second_tour.txt", "w")
second_tour.write(str(count_player) + "\n")

i = 0
for key, value in new_dict.items():
    i += 1
    second_tour.write("{}) {} {} {}\n".format(i, key[0], key[1], value))
second_tour.close()

# зачёт!
