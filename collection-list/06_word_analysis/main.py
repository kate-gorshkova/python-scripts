word = input("Введите слово: ")
word_list = []  # список получился лишний.
count = 0
for letter in word:
    j = 0
    for checked_letter in word:
        if letter == checked_letter:
            j += 1
    if j == 1:
        count += 1
print(count)

# зачёт!
