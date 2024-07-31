import json
import os
from typing import Dict, List
from src.external_api import get_exchange_rate


def load_transactions(file_path: str) -> List[Dict]:
    """
    Функция для загрузки данных о финансовых транзакциях из JSON-файла.
    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о финансовых транзакциях либо пустой список.
    """
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        print(f"Файл {file_path} не существует или не является файлом.")
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            return []
        return data
    except (json.JSONDecodeError, ValueError):
        return []


file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
transactions = load_transactions(file_path)
print(transactions)


def convert_transaction_to_rub(transaction: Dict) -> str:
    """
    Перевод в рубли с помошью API
    :param transaction: список транзакций
    :return: выводим сумму транзакций в рублях
    """
    amount_str = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError(f"Некорректное значение суммы: {amount_str}")

    TO_CURRENCY = "RUB"

    if currency == TO_CURRENCY:
        return f"{amount} {TO_CURRENCY}"
    elif currency in ["USD", "EUR"]:
        exchange_rate = get_exchange_rate(currency, TO_CURRENCY)
        return f"{amount} {currency} = {amount * exchange_rate} {TO_CURRENCY}"
    else:
        raise ValueError(f"Неподдерживаемая валюта: {currency}")


converted_amounts = []
for trans in transactions:
    try:
        converted_amount = convert_transaction_to_rub(trans)
        converted_amounts.append(converted_amount)
        print(converted_amount)
    except ValueError as e:
        print(e)
