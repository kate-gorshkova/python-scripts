text = input("Введите текст: ")
file_text = open("text.txt", "w")
file_text.write(text)

length_text = 0
for i_sym in text:
    if i_sym.isalpha():
        length_text += 1

letter_dict = dict()

for i_sym in text.lower():
    if i_sym.isalpha():
        if i_sym not in letter_dict:
            letter_dict[i_sym] = 1
        else:
            letter_dict[i_sym] += 1

analysis_file = open("analysis.txt", "w")

res = sorted(letter_dict.items(), key=lambda x: (-x[1], x[0]))

for i_tuple in res:
    analysis_file.write("{} {}\n".format(i_tuple[0], round(int(i_tuple[1]) / length_text, 3)))
analysis_file.close()

# зачёт!
