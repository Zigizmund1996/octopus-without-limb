import re

from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(data: str) -> str:
    """
    Функция маскирует данные карты и счета из строк

    """

    numbers = re.findall(r"\b\d+\b", data)
    for number in numbers:
        if len(number) == 16:
            mask_number = get_mask_card_number(number)
        elif len(number) == 20:
            mask_number = get_mask_account(number)
        else:
            mask_number = "Ошибка"
        data = re.sub(number, mask_number, data, count=1)
    return data


def get_date(date_str: str) -> str:
    """
    Приводит строку с датой к нужному формату

    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"

