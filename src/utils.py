import json
import logging
import os
from typing import Dict, List

from src.external_api import get_exchange_rate

project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
log_directory = os.path.join(project_root, "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
log_file = os.path.join(log_directory, "utils.log")

file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict]:
    """
    Функция для загрузки данных о финансовых транзакциях из JSON-файла.
    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о финансовых транзакциях либо пустой список.
    """
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        logger.error(f"Файл {file_path} не существует или не является файлом.")
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            logger.error(f"Данные из файла {file_path} не являются списком.")
            return []
        logger.info(f"Файл {file_path} успешно загружен.")
        return data
    except (json.JSONDecodeError, ValueError) as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
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
        error_message = f"Некорректное значение суммы: {amount_str}"
        logger.error(error_message)
        raise ValueError(error_message)

    TO_CURRENCY = "RUB"

    if currency == TO_CURRENCY:
        return f"{amount} {TO_CURRENCY}"
    elif currency in ["USD", "EUR"]:
        try:
            exchange_rate = get_exchange_rate(currency, TO_CURRENCY)
            return f"{amount} {currency} = {amount * exchange_rate} {TO_CURRENCY}"
        except Exception as e:
            error_message = f"Ошибка при получении курса обмена: {e}"
            logger.error(error_message)
            raise ValueError(error_message)
    else:
        error_message = f"Неподдерживаемая валюта: {currency}"
        logger.error(error_message)
        raise ValueError(error_message)


converted_amounts = []
for trans in transactions:
    try:
        converted_amount = convert_transaction_to_rub(trans)
        converted_amounts.append(converted_amount)
        print(converted_amount)
        logger.info(f"Успешная конвертация: {converted_amount}")
    except ValueError as e:
        logger.error(e)
        print(e)
