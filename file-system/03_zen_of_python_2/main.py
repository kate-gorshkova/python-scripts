zen_python = open("zen.txt")

line_count = 0
sym_count = 0
word_count = 0
for line in zen_python:
    for i_sym in line:
        if i_sym.isalpha():
            sym_count += 1
        if i_sym == " " or i_sym == "\n":
            word_count += 1
    line_count += 1
print("Количество букв: {}".format(sym_count))
print("Количество слов: {}".format(word_count))
print("Количество строк: {}".format(line_count))

zen_python.close()

# зачёт!
