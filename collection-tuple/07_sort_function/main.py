def sort_function(any_tuple):
    for value in any_tuple:
        if not isinstance(value, int):
            return any_tuple

    return tuple(sorted(any_tuple))


my_tuple = (1, 2, 3, 4, 3, 10, 1, 3)
print(sort_function(my_tuple))

# зачёт!
