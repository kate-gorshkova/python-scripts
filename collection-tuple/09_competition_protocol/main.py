def total_result(any_tuple):
    return any_tuple[1][0] * 1000000 - any_tuple[1][1]


records_count = int(input("Сколько записей вносится в протокол? "))
data_base = dict()
total_list = []
print("Записи (результат и имя):")
for i_record in range(1, records_count + 1):
    print("{record} запись:".format(record=i_record), end=" ")
    result_nickname = list(input().split())
    res_nick = int(result_nickname[0])
    nick = result_nickname[1]
    my_tuple = (res_nick, i_record)
    total_list = []
    if nick in data_base:
        total_list = data_base.get(nick)
        if my_tuple[0] > int(total_list[0]):
            data_base[nick] = my_tuple
    else:
        data_base[nick] = my_tuple

sort_list = sorted(data_base.items(), key=total_result, reverse=True)

print("\nИтоги соревнований:")
for index, score in enumerate(sort_list):
    if index == 3:
        break
    print("{num_place} место. {name} ({i_score})".format(num_place=index + 1, name=score[0], i_score=score[1][0]))

# зачёт!
