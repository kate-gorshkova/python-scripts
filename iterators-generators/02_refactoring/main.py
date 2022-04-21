from collections.abc import Iterable


def num_square_gen(find: int, list1: list, list2: list) -> Iterable[int]:
    for x in list1:
        for y in list2:
            if x * y == find:
                yield x, y, x * y
                break


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
gen = num_square_gen(to_find, list_1, list_2)
for elem in gen:
    print(elem)

# зачёт!