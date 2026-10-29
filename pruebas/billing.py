import httpx


def fetch_invoice_total(invoice_id: str) -> float:
    """Returns the invoice total from the billing API, or 0 if the call fails."""
    try:
        response = httpx.get(f"https://billing.example.com/invoices/{invoice_id}")
        response.raise_for_status()
        return response.json()["total"]
    except Exception:
        return 0.0
