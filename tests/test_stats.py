from decimal import Decimal

from shop.stats import average_ticket, best_day


def test_average_ticket_is_the_mean_of_the_totals():
    assert average_ticket([Decimal("10"), Decimal("20")]) == Decimal("15")


def test_average_ticket_of_a_day_without_carts_is_zero():
    assert average_ticket([]) == Decimal("0")


def test_best_day_is_the_one_with_the_most_sales():
    assert best_day({"lunes": Decimal("10"), "martes": Decimal("20")}) == "martes"


def test_best_day_without_sales_is_none():
    assert best_day({}) is None
