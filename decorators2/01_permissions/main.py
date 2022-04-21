from typing import Callable
from typing import Optional
import functools


def check_permission(_func: Optional[Callable] = None, *, user_permissions: str = None) -> Callable:
    def permission_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> str:
            """ Декоратор, который проверяет, есть ли у пользователя доступ к вызываемой функции """
            try:
                if user_permissions == "admin":
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError as err:
                print("{}. У пользователя недостаточно прав, чтобы выполнить функцию {}".format(
                    err.__class__.__name__, func.__name__)
                )

        return wrapped_func

    if _func:
        return permission_decorator(_func)
    return permission_decorator


@check_permission(user_permissions="admin")
def delete_site():
    print("Удаляем сайт")


@check_permission(user_permissions="user_1")
def add_comment():
    print("Добавляем комментарий")


delete_site()
add_comment()

# зачёт!
