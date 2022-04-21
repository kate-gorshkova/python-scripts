import functools
from typing import Callable


def counter(func: Callable) -> Callable:
    """ Декоратор, считающий и выводящий количество вызовов """

    @functools.wraps(func)
    def wrapper_counter(*args, **kwargs):
        wrapper_counter.count += 1
        result = func(*args, **kwargs)
        print("Функция {} была вызвана {} раз(а)".format(func.__name__, wrapper_counter.count))
        return result

    wrapper_counter.count = 0
    return wrapper_counter


@counter
def summa(num: int) -> int:
    my_sum = sum(i_num for i_num in range(1, num + 1))
    return int(my_sum)


summa(2)
summa(3)
summa(4)

# зачёт!
