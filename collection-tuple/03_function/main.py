def function(my_tuple, item):
    if item in my_tuple:
        if my_tuple.count(item) > 1:
            first_index = my_tuple.index(item)
            second_index = my_tuple.index(item, first_index + 1) + 1
            total_tuple = my_tuple[first_index:second_index]
            print(total_tuple)
        else:
            print(my_tuple[my_tuple.index(item):])
    else:
        return print(())


elem = input("Введите любой элемент: ")
our_tuple = ("1", "2", "3", "4", "5", "2", "3", "4")
function(our_tuple, elem)

# зачёт!
