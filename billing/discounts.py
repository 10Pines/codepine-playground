"""Discounts on a customer's invoices."""


def discount(total: float, percentage: int) -> float:
    """The total with `percentage` off: from 0 to 100."""
    if not 0 <= percentage <= 100:
        raise ValueError("A discount goes from 0% to 100%")
    return total - total * percentage / 100


def best_discount(discounts: list[int]) -> int:
    """The largest of the discounts; 0 without discounts."""
    return max(discounts, default=0)
