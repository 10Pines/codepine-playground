"""Prices of a shopping cart: its subtotal, the volume discount and the total to pay."""

from decimal import Decimal

# Carts from this amount on get the volume discount.
VOLUME_DISCOUNT_THRESHOLD = Decimal("100")
VOLUME_DISCOUNT_RATE = Decimal("0.10")


def subtotal(items: list[dict]) -> Decimal:
    """The sum of each item's price times its quantity."""
    return sum(
        (Decimal(str(item["price"])) * item["quantity"] for item in items),
        Decimal("0"),
    )


def volume_discount(amount: Decimal) -> Decimal:
    """10 % off for carts of 100 or more."""
    if amount >= VOLUME_DISCOUNT_THRESHOLD:
        return amount * VOLUME_DISCOUNT_RATE
    return Decimal("0")


def total(items: list[dict]) -> Decimal:
    """What the customer pays: the subtotal minus the volume discount."""
    amount = subtotal(items)
    return amount - volume_discount(amount)
