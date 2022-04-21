from typing import Callable
import functools

app = {}


def callback(any_route: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        app[any_route] = func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            ret = func(*args, **kwargs)
            return ret

        return wrapped

    return wrapper


@callback("//")
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# зачёт!
