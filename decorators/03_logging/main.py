from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Callable:
    """ Декоратор, отвечающий за логирование функций """

    @functools.wraps(func)
    def wrapper_logging(*args, **kwargs) -> Any:
        try:
            f = func(*args, **kwargs)
            print("Название функции: {}\nДокументация: {}".format(
                func.__name__, func.__doc__
            ))
            return f
        except Exception as e:
            with open("function_errors.log", "a", encoding="utf-8") as file_errors:
                file_errors.write("Название функции: {}"
                                  "\nОшибка: {}"
                                  "\nДата возникновения ошибки: {}"
                                  "\nВремя возникновения ошибки: {}\n\n".format(func.__name__,
                                                                                e,
                                                                                datetime.date.today(),
                                                                                datetime.datetime.now().time()
                                                                                ))

    return wrapper_logging


@logging
def div(a: int, b: int) -> float:
    """
    Функция деления одного числа на другое
    :return: частное двух чисел
    """

    return a / b


div(5, 20)
div(20, 2)
div(10, 0)
div(30, 10)
div(0, 50)
div(100, 0)
div(20, 5)
div(0, 0)

# зачёт!
