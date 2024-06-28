from functools import lru_cache
from time import sleep


@lru_cache(maxsize=1)
def _get_all_admins() -> list[int]:
    admins = []
    return admins


def is_admin(user_id) -> bool:
    # return user_id in _get_all_admins()
    return True  # Заменить на верхнюю строку, после написания функционала для получения списка админов
