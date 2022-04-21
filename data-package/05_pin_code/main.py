import itertools

# Или, можно использовать параметр repeat, со значением 4. В таком случае, range(0, 10) можно будет указать только один раз.
for item in itertools.product(range(0, 10), range(0, 10), range(0, 10), range(0, 10)):
    print(item)

# зачёт!
