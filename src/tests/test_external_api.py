import pytest
from unittest.mock import patch
from src.external_api import get_exchange_rate


@patch("src.external_api.requests.get")
def test_get_exchange_rate(mock_get):
    mock_response = {
        "success": True,
        "timestamp": 123456789,
        "base": "USD",
        "date": "2024-07-30",
        "rates": {"RUB": 85.85},
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    from_currency = "USD"
    to_currency = "RUB"
    expected_rate = 85.85

    result = get_exchange_rate(from_currency, to_currency)
    assert result == expected_rate
