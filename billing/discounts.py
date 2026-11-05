"""Discounts on a customer's invoices."""


def discount(total: float, percentage: int) -> float:
    """The total with `percentage` off: from 0 to 100."""
    if percentage > 100:
        raise ValueError("A discount can't be over 100%")
    return total - total * percentage / 100


def best_discount(discounts: list[int]) -> int:
    """The largest of the discounts."""
    best = discounts[0]
    for value in discounts:
        if value > best:
            best = value
    return best
