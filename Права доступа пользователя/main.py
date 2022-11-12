from typing import Callable, Any
import functools


def check_permission(user: str):
    """
    Декоратор проверки прав пользователя для вызова функции,
    передающий аргумент группы пользователя
    """
    def check(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args: Any) -> [Callable, str]:
            try:
                if user in user_permissions:
                    func(*args)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapped
    return check


user_permissions = ['admin']


@check_permission('admin')
def delete_site() -> None:
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


delete_site()
add_comment()
