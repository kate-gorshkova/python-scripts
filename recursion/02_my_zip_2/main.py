def min_count(any_string, any_tuple):
    return min(len(any_string), len(any_tuple))


def func(any_str, any_tuple):
    generator = ((any_str[i_sym], any_tuple[i_sym]) for i_sym in range(min_count(any_str, any_tuple)))
    return generator, print(generator)


my_str = "abcdaaa"
my_tuple = (10, 20, 30, 40)

for pair in func(my_str, my_tuple)[0]:
    print(pair)

# зачёт!
