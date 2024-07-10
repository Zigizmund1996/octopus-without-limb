from typing import Dict, List

from src.widget import get_date

test = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_dist: List[Dict], state: str ="EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа state.
    :param list_dist: список словарей
    :param state:значение ключа state для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей,
    у которых ключ state соответствует указанному значению
    """
    filter_list = []
    for dist in list_dist:
        if dist.get("state") == state:
            filter_list.append(dist)
    return filter_list


def sort_by_date(filter_by_state: List[Dict], decrease: bool = True) -> List[Dict]:
    """
    Функция сортирует список словарей по дате
    :param filter_by_state: функция приводит формат даты
    :return: отсортированный список словарей
    """
    sorted_list = []
    for dist in filter_by_state:
        dist["date"] = get_date(dist["date"])
    sorted_list = sorted(filter_by_state, key=lambda x: x["date"], reverse=decrease)
    return sorted_list


print(filter_by_state(test))
print(sort_by_date(filter_by_state(test)))
