def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


text = input("Введите текст: ").lower()
hist = histogram(text)
print("Оригинальный словарь частот:")
for i_sym in sorted(hist.keys()):
    print(i_sym, ":", hist[i_sym])

new_list = list(set(list(hist.values())))

print("\nИнвертированный словарь частот:")
for i in range(len(new_list)):
    my_list = []
    for my_key in hist.keys():
        if new_list[i] == hist.get(my_key):
            my_list.append(my_key)
    print(new_list[i], ":", my_list)

# зачёт!
