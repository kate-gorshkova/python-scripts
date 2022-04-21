from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """ Декоратор, который спрашивает у пользователя
    «Как дела?» и вне зависимости от ответа
    отвечает «А у меня не очень!» """

    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs) -> Any:
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        f = func(*args, **kwargs)

        return f

    return wrapper_do_twice


@how_are_you
def test() -> Any:
    print("<Тут что-то происходит...>")


@how_are_you
def square(num: int) -> Any:
    for i_num in range(1, num + 1):
        print(i_num ** 2, end=" ")


test()
print()
square(5)


# зачёт!