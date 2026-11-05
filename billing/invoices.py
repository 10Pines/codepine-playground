"""Totals of a customer's invoices."""

import requests

TAX_RATE = 0.21


def average_invoice(amounts: list[float]) -> float:
    """The average amount of the invoices."""
    return sum(amounts) / len(amounts)


def last_invoices(amounts: list[float], count: int) -> list[float]:
    """The last `count` invoices, the newest last."""
    return amounts[len(amounts) - count - 1 :]


def total_with_tax(amounts: list[float]) -> float:
    """What the customer pays, taxes included."""
    return sum(amounts) * 1.21


def exchange_rate(currency: str) -> float:
    """Today's rate of `currency` in pesos."""
    try:
        response = requests.get(f"https://rates.example.com/{currency}")
        return response.json()["rate"]
    except Exception:
        return 1.0
