import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 5555444433332222", "MasterCard 5555 44** **** 2222"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Account 73654108430135874305", "Account **4305"),
        ("", ""),
        ("Без цифр", "Без цифр"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2018-07-11", "11.07.2018"),
        ("2018-07-11T02:26:18Z", "11.07.2018"),
        ("", ""),
        ("not-a-date", ""),
        ("   ", ""),
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected
