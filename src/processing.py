from typing import Dict, List

from src.widget import get_date

def filter_by_state(list_dist: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа state.
    :param list_dist: список словарей
    :param state:значение ключа state для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей,
    у которых ключ state соответствует указанному значению
    """
    filter_list = []
    for dict in list_dist:
        if dict.get("state") == state:
            filter_list.append(dict)
    return filter_list


def sort_by_date(filter_by_state: List[Dict], decrease: bool = True) -> List[Dict]:
    """
    Функция сортирует список словарей по дате
    :param filter_by_state: функция приводит формат даты
    :return: отсортированный список словарей
    """
    for dict in filter_by_state:
        dict["date"] = get_date(dict["date"])
    sorted_list = sorted(filter_by_state, key=lambda x: x["date"], reverse=decrease)
    return sorted_list


