from __future__ import annotations

import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

_ANY_DIGIT_RE = re.compile(r"\d")


def mask_account_card(value: str) -> str:
    """
    Принимает строку вида:
    - "Visa Platinum 7000792289606361" -> "Visa Platinum 7000 79** **** 6361"
    - "Счет 73654108430135874305" -> "Счет **4305"

    Если не удаётся распознать/замаскировать — возвращает исходную строку.
    """
    if not value or not _ANY_DIGIT_RE.search(value):
        return value

    digits_only = re.sub(r"\D", "", value)

    is_account = value.strip().lower().startswith(
        ("счет", "account")
    ) or len(digits_only) > 16
    if is_account:
        masked = get_mask_account(value)
        if not masked:
            return value
        prefix = value.split()[0]
        return f"{prefix} {masked}"

    masked = get_mask_card_number(value)
    if not masked:
        return value

    name_part = value.rstrip()
    m = re.search(r"\d", name_part)
    if not m:
        return value
    prefix = name_part[: m.start()].rstrip()
    return f"{prefix} {masked}".strip()


def get_date(value: str) -> str:
    """
    Преобразует дату из ISO-формата к 'DD.MM.YYYY'.
    Пример: '2018-07-11T02:26:18.671407' -> '11.07.2018'
    Некорректная/пустая строка -> ''.
    """
    if not value:
        return ""

    raw = value.strip()
    if not raw:
        return ""

    candidate = raw.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(candidate)
    except ValueError:
        return ""
    return dt.strftime("%d.%m.%Y")
