from typing import Callable, Any
import functools
import time


def slow_down(func: Callable) -> Callable:
    """ Декоратор, который ждёт несколько секунд """

    @functools.wraps(func)
    def wrapper_slow_down(sec: int, *args, **kwargs) -> Any:
        time.sleep(sec)
        f = func(*args, **kwargs)

        return f

    return wrapper_slow_down


@slow_down
def test() -> Any:
    print("Выполняю!")


print("Жду {} секунд(у/ы) и выполняю.".format(5))
test(5)

# зачёт!
