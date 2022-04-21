def flatten(any_list):
    if not any_list:
        return any_list
    elif isinstance(any_list[0], list):
        return flatten(any_list[0]) + flatten(any_list[1:])
    else:
        return [any_list[0]] + flatten(any_list[1:])


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(flatten(nice_list))

# зачёт!
