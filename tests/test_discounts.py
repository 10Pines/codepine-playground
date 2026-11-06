import pytest

from billing.discounts import best_discount, discount


@pytest.mark.parametrize(("percentage", "total"), [(0, 200.0), (25, 150.0), (100, 0.0)])
def test_takes_the_percentage_off(percentage, total):
    assert discount(200.0, percentage) == total


@pytest.mark.parametrize("percentage", [-1, 101])
def test_rejects_a_percentage_out_of_range(percentage):
    with pytest.raises(ValueError):
        discount(200.0, percentage)


@pytest.mark.parametrize(
    ("discounts", "best"), [([10, 30, 20], 30), ([-5, -1], -1), ([], 0)]
)
def test_returns_the_largest_discount(discounts, best):
    assert best_discount(discounts) == best
