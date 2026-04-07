from __future__ import annotations

from datetime import datetime
from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]],
    state: str = "EXECUTED",
) -> list[dict[str, Any]]:
    """Фильтрует операции по значению ключа 'state'."""
    return [op for op in operations if op.get("state") == state]


def _parse_iso_date(value: Any) -> datetime:
    if not isinstance(value, str):
        return datetime.min
    candidate = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(candidate)
    except ValueError:
        return datetime.min


def sort_by_date(
    operations: list[dict[str, Any]],
    reverse: bool = True,
) -> list[dict[str, Any]]:
    """
    Сортирует операции по ключу 'date' (ISO-строка).
    Некорректные даты считаются минимальными.
    """
    return sorted(
        operations,
        key=lambda op: _parse_iso_date(op.get("date")),
        reverse=reverse,
    )
