from typing import Callable, Any
import functools


def debug(func: Callable) -> Callable:
    """ Декоратор, котоый выводит имя функции и возвращаемое значение """

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs) -> Any:
        my_args = [f'"{arg}"' for arg in args]
        my_kwargs = [f'{k}={v}' if isinstance(v, int) else f'{k}="{v}"' for k, v in kwargs.items()]
        print("Вызывается {}({})".format(func.__name__, ", ".join(my_args + my_kwargs)))

        res = func(*args, **kwargs)
        print('"{}" вернула значение "{}"'.format(func.__name__, res))
        print(res, end="\n\n")
        return res

    return wrapper_debug


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# зачёт!
