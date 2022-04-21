file = open('numbers.txt', 'r')
summa = 0
for i_line in file:
    for elem in i_line:
        if elem.isdigit():
            summa += int(i_line)

summa_str = str(summa)
file.close()
print(summa_str)

counts_file = open("answer.txt", "w")
counts_file.write(summa_str)
counts_file.close()

# зачёт!
