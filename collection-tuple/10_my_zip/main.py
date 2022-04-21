def min_count(any_string, any_tuple):
    return min(len(any_string), len(any_tuple))


my_str = "abcd"
my_tuple = (10, 20, 30, 40)

generator = ((my_str[i_sym], my_tuple[i_sym]) for i_sym in range(min_count(my_str, my_tuple)))
print(generator)
for pair in generator:
    print(pair)

# зачёт!
