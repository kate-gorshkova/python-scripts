stroke = input("Введите строку: ")
stroke += " "
my_stroke = ""
total_stroke = ""
for i_letter in range(len(stroke) - 1):
    if stroke[i_letter] == stroke[i_letter + 1]:
        my_stroke += stroke[i_letter]
    else:
        my_stroke += stroke[i_letter + 1]
        total_stroke += stroke[i_letter] + str(len(my_stroke))
        my_stroke = ""
print(total_stroke)

# зачёт!
