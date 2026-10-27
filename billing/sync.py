"""Sends invoices to the accounting system and reads exchange rates."""

import logging

import httpx

logger = logging.getLogger(__name__)

ACCOUNTING_URL = "https://accounting.example.com/api/invoices"
RATES_URL = "https://rates.example.com/api/latest"


def sync_invoices(invoices: list[dict]) -> int:
    """Sends each invoice to the accounting system. Returns how many were sent."""
    sent = 0
    for invoice in invoices:
        try:
            response = httpx.post(ACCOUNTING_URL, json=invoice, timeout=10)
            response.raise_for_status()
            sent += 1
        except Exception:
            pass
    return sent


def latest_rate(currency: str, timeout: float = 5) -> float:
    """The latest exchange rate from the currency to US dollars."""
    response = httpx.get(RATES_URL, params={"from": currency, "to": "USD"}, timeout=timeout)
    response.raise_for_status()
    return float(response.json()["rate"])
