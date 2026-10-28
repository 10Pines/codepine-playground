import requests

STOCK_URL = "https://stock.example.com/items"


def reserve(item_id: str, quantity: int) -> bool:
    """Reserves the quantity of the item in the stock service; whether it could."""
    try:
        response = requests.post(f"{STOCK_URL}/{item_id}/reservations", json={"quantity": quantity})
        response.raise_for_status()
        return True
    except Exception:
        return False
