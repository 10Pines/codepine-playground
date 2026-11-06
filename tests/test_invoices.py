from unittest.mock import Mock

import pytest
import requests

from billing import invoices


def test_averages_the_invoices():
    assert invoices.average_invoice([100.0, 200.0]) == 150.0


def test_averages_no_invoices_as_zero():
    assert invoices.average_invoice([]) == 0.0


@pytest.mark.parametrize(
    ("count", "last"),
    [(0, []), (2, [20.0, 30.0]), (3, [10.0, 20.0, 30.0]), (5, [10.0, 20.0, 30.0])],
)
def test_returns_the_last_invoices(count, last):
    assert invoices.last_invoices([10.0, 20.0, 30.0], count) == last


def test_adds_the_tax_to_the_total():
    assert invoices.total_with_tax([100.0, 100.0]) == pytest.approx(242.0)


def test_reads_the_rate_from_the_service(monkeypatch):
    get = Mock(return_value=Mock(json=lambda: {"rate": 1450.5}))
    monkeypatch.setattr(requests, "get", get)

    assert invoices.exchange_rate("USD") == 1450.5
    get.assert_called_once_with("https://rates.example.com/USD", timeout=5)


def test_raises_when_the_service_fails(monkeypatch):
    response = Mock()
    response.raise_for_status.side_effect = requests.HTTPError("503")
    monkeypatch.setattr(requests, "get", Mock(return_value=response))

    with pytest.raises(requests.HTTPError):
        invoices.exchange_rate("USD")
