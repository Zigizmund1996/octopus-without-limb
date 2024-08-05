import logging
import os

import pandas as pd
from pandas import DataFrame

# создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# вывод в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# форматтер
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
# обработчик
logger.addHandler(console_handler)


def read_csv(file_path: str) -> DataFrame:
    """
    Считывает данные из CSV-файла.
    :param file_path: Путь к CSV-файлу.
    :return: DataFrame с данными.
    """
    try:
        transactions_csv = pd.read_csv(file_path)
        logger.info(f"Успешно считаны данные из CSV-файла: {file_path}")
        return transactions_csv
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла: {e}")
        raise


def read_excel(file_path: str) -> DataFrame:
    """
    Считывает данные из XLSX-файла.
    :param file_path: Путь к XLSX-файлу.
    :return: DataFrame с данными.
    """
    try:
        transactions_xlsx = pd.read_excel(file_path, engine="openpyxl")
        logger.info(f"Успешно считаны данные из XLSX-файла: {file_path}")
        return transactions_xlsx
    except Exception as e:
        logger.error(f"Ошибка при чтении XLSX-файла: {e}")
        raise


if __name__ == "__main__":  # для того что бы когда мы запускали код напрямую из файла для проверки
    csv_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
    xlsx_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")

    print(read_csv(csv_file_path).head())
    print(read_excel(xlsx_file_path).head())
