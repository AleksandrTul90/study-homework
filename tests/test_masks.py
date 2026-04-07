import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
        ("", ""),
        ("No digits here", ""),
        ("12345678", "12345678"),
        ("123456789", "1234*6789"),
        ("123456789012345", "1234*******2345"),
    ],
)
def test_get_mask_card_number(value: str, expected: str) -> None:
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Счет 73654108430135874305", "**4305"),
        ("73654108430135874305", "**4305"),
        ("1234", "**1234"),
        ("12", "**12"),
        ("", ""),
        ("Account", ""),
    ],
)
def test_get_mask_account(value: str, expected: str) -> None:
    assert get_mask_account(value) == expected
