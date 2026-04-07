import pytest


@pytest.fixture()
def operations_sample() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582"},
        {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "EXECUTED", "date": "2020-01-01T00:00:00.000000"},
        {"id": 4, "state": "PENDING", "date": "not-a-date"},
        {"id": 5, "state": "EXECUTED", "date": ""},
        {"id": 6, "state": None, "date": None},
    ]


@pytest.fixture()
def card_numbers() -> dict[str, str]:
    return {
        "plain16": "7000792289606361",
        "spaced16": "7000 7922 8960 6361",
        "named16": "Visa Platinum 7000792289606361",
        "short": "12345678",
        "odd": "123456789012345",
        "nodigits": "Visa Platinum",
    }
