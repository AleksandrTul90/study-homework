import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state", ["EXECUTED", "CANCELED", "PENDING"])
def test_filter_by_state_parametrized(
    operations_sample: list[dict], state: str
) -> None:
    result = filter_by_state(operations_sample, state=state)
    assert all(op.get("state") == state for op in result)


def test_filter_by_state_when_no_matches() -> None:
    ops = [{"state": "EXECUTED"}, {"state": "CANCELED"}]
    assert filter_by_state(ops, state="PENDING") == []


@pytest.mark.parametrize("reverse", [True, False])
def test_sort_by_date_orders(operations_sample: list[dict], reverse: bool) -> None:
    sorted_ops = sort_by_date(operations_sample, reverse=reverse)

    ids = [op["id"] for op in sorted_ops]
    if reverse:
        assert ids.index(3) < ids.index(1)  # 2020 ahead of 2019
        assert ids.index(1) < ids.index(2)  # 2019 ahead of 2018
    else:
        assert ids.index(2) < ids.index(1)  # 2018 before 2019
        assert ids.index(1) < ids.index(3)  # 2019 before 2020


def test_sort_by_date_handles_invalid_dates() -> None:
    ops = [
        {"id": 1, "date": "not-a-date"},
        {"id": 2, "date": "2019-01-01T00:00:00"},
        {"id": 3, "date": None},
    ]
    sorted_ops = sort_by_date(ops, reverse=True)
    assert [op["id"] for op in sorted_ops][:1] == [2]
