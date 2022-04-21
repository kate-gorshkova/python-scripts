from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *any_args, **any_kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        print("Переданные арги и кварги в декоратор:", any_args, any_kwargs)
        return func(*args, **kwargs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


decorated_function("Юзер", 101)

# зачёт!
