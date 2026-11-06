from decimal import Decimal

from shop.pricing import subtotal, total


def test_subtotal_adds_each_item_times_its_quantity():
    items = [{"price": 10, "quantity": 2}, {"price": 5.5, "quantity": 1}]
    assert subtotal(items) == Decimal("25.5")


def test_total_without_discount_is_the_subtotal():
    assert total([{"price": 40, "quantity": 1}]) == Decimal("40")


def test_total_of_a_big_cart_has_the_volume_discount():
    assert total([{"price": 200, "quantity": 1}]) == Decimal("180")


def test_a_cart_of_exactly_the_threshold_has_the_volume_discount():
    assert total([{"price": 100, "quantity": 1}]) == Decimal("90")
