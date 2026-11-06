"""Sales numbers for the store's daily report."""

from decimal import Decimal


def average_ticket(totals: list[Decimal]) -> Decimal:
    """The average amount of the day's carts."""
    return sum(totals, Decimal("0")) / len(totals)


def best_day(sales_by_day: dict[str, Decimal]) -> str:
    """The day with the most sales."""
    return max(sales_by_day, key=lambda day: sales_by_day[day])
