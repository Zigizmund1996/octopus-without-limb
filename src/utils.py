import json
import os
from typing import List


# file_path = os.path.join('data', 'operations.json')
def load_transactions(file_path: str) -> List:
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
        if not isinstance(data, List):
            return []
        return data
    except (json.JSONDecodeError, ValueError):
        return []


file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"data", "operations.json")
transaction = load_transactions(file_path)
print(transaction)
