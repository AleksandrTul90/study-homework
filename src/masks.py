from __future__ import annotations

import re

_DIGITS_RE = re.compile(r"\d+")


def _extract_digits(value: str) -> str:
    parts = _DIGITS_RE.findall(value)
    return "".join(parts)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.

    Основной кейс (16 цифр): XXXX XX** **** XXXX (с пробелами как в примере).
    Если цифр нет — возвращает пустую строку.
    Если длина нестандартная — маскирует «середину», оставляя первые 4 и последние
    4.
    """
    digits = _extract_digits(card_number)
    if not digits:
        return ""

    if len(digits) == 16:
        return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"

    if len(digits) <= 8:
        return digits

    head = digits[:4]
    tail = digits[-4:]
    middle_mask = "*" * (len(digits) - 8)
    return f"{head}{middle_mask}{tail}"


def get_mask_account(account: str) -> str:
    """
    Маскирует номер счета: **XXXX (последние 4 цифры).
    Если цифр нет — возвращает пустую строку.
    """
    digits = _extract_digits(account)
    if not digits:
        return ""
    return f"**{digits[-4:]}"
