import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [("7000792289606361", "7000 79** **** 6361")])
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    masked_card = get_mask_card_number(card_number)
    assert masked_card == expected


@pytest.mark.parametrize("account_number, expected", [("73654108430135874305", "**4305")])
def test_get_mask_account(account_number: str, expected: str) -> None:
    masked_account = get_mask_account(account_number)
    assert masked_account == expected
