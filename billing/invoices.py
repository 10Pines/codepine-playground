"""Totals of a customer's invoices."""

import requests

TAX_RATE = 0.21
# How long the rates service has to answer before giving up.
RATES_TIMEOUT_SECONDS = 5


def average_invoice(amounts: list[float]) -> float:
    """The average amount of the invoices; 0 without invoices."""
    return sum(amounts) / len(amounts) if amounts else 0.0


def last_invoices(amounts: list[float], count: int) -> list[float]:
    """The last `count` invoices, the newest last; all of them if there are fewer."""
    return amounts[max(len(amounts) - count, 0) :]


def total_with_tax(amounts: list[float]) -> float:
    """What the customer pays, taxes included."""
    return sum(amounts) * (1 + TAX_RATE)


def exchange_rate(currency: str) -> float:
    """Today's rate of `currency` in pesos. Raises requests' error if the service fails."""
    response = requests.get(
        f"https://rates.example.com/{currency}", timeout=RATES_TIMEOUT_SECONDS
    )
    response.raise_for_status()
    return response.json()["rate"]
