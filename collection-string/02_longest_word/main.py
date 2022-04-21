phrase = input("Введите фразу: ").split()
lengths_list = [len(word) for word in phrase]
print("Самое длинное слово:", phrase[lengths_list.index(max(lengths_list))])
print("Длина слова:", max(lengths_list))

# зачёт!
