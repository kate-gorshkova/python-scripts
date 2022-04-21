import functools
import time
from typing import Callable


def timer(func: Callable, date_format, cls) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        start = time.time()
        print("-Запускается '{}.{}'. Дата и время запуска: ".format(cls.__name__, func.__name__), end="")
        my_date = ""
        for i in date_format:
            if i.isalpha():
                my_date += "%" + i
            else:
                my_date += i
        print(time.strftime(my_date))
        result = func(*args, **kwargs)
        end = time.time()
        print("-Завершение '{}.{}'. Время работы функции:".format(cls.__name__, func.__name__), end - start)
        return result

    return wrapped


def log_methods(date_format: str = None) -> Callable:
    def wrapper(cls):

        for i_method_name in dir(cls):
            if i_method_name.startswith("__") is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = timer(cur_method, date_format, cls)
                setattr(cls, i_method_name, decorated_method)
        return cls

    return wrapper


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# зачёт!
