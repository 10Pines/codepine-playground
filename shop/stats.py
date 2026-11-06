"""Sales numbers for the store's daily report."""

from decimal import Decimal


def average_ticket(totals: list[Decimal]) -> Decimal:
    """The average amount of the day's carts, or 0 if there were none."""
    if not totals:
        return Decimal("0")
    return sum(totals, Decimal("0")) / len(totals)


def best_day(sales_by_day: dict[str, Decimal]) -> str | None:
    """The day with the most sales, or None if there were no sales."""
    if not sales_by_day:
        return None
    return max(sales_by_day, key=lambda day: sales_by_day[day])
