from collections.abc import Iterable

N = int(input("Введите число: "))

# Генераторное выражение
num_square = (i_num ** 2 for i_num in range(1, N + 1))
for i_num_square in num_square:
    print(i_num_square, end=" ")
print()


# Генератор
def num_square_gen(num: int) -> Iterable[int]:
    for i_num in range(1, num + 1):
        yield i_num ** 2


gen = num_square_gen(N)
for elem in gen:
    print(elem, end=" ")
print()


# Итератор
class SquareIterator:
    def __init__(self, n: int) -> None:
        self.n = n
        self.num = 0

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> int:
        if self.num < self.n:
            self.num += 1
            return self.num ** 2

        raise StopIteration


num_iterator = SquareIterator(N)
for i_num in num_iterator:
    print(i_num, end=" ")

# зачёт!
