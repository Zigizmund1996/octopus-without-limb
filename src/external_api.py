import os
from typing import Dict, Any

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.apilayer.com/exchangerates_data/latest"
API_KEY = os.getenv("API_KEY")


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Функция делает запрос к API и получает актуальный курс валюты
    :param from_currency: код валюты которую хотим перевести
    :param to_currency: код валюты в какую волюту хотим перевести
    :return: курс валюты
    """
    headers = {"apikey": API_KEY}
    params = {"base": from_currency, "symbols": to_currency}
    response = requests.get(URL, headers=headers, params=params)
    data: Dict[str, Any] = response.json()
    round_data = round(data["rates"][to_currency], 2)
    return float(round_data)
