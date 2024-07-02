import re

from masks import get_mask_account, get_mask_card_number

date = "2024-03-11T02:26:18.671407"
input_data = """Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305"""


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


test = print(mask_account_card(input_data))
test_date = print(get_date(date))
