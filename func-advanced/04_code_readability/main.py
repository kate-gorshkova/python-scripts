print([x for x in range(2, 1000) if not [n for n in range(2, x) if not x % n]])

prime = []

# Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i" и "j" не отражают. В нашем случае, "i" и "j" это не Индексы.
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

print(prime)

# зачёт!
