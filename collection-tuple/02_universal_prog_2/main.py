def is_instance(item, my_type):
    if type(item) == my_type:
        return [sym for index, sym in enumerate(item) if is_prime(index)]
    return False


def is_prime(my_id):
    flag = 0
    for num in range(1, my_id + 1):
        if my_id % num == 0:
            flag += 1
    if flag == 2:
        return True

    return False


elem = [1, 3, 5, 3, 6, [1, 2, 4]]
if list_item := is_instance(elem, str):
    print(list_item)
elif list_item := is_instance(elem, list):
    print(list_item)
elif list_item := is_instance(elem, tuple):
    print(list_item)
elif list_item := is_instance(elem, dict):
    print(list_item)

# зачёт!
