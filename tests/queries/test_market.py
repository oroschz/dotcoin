from dotcoin.context import fetch
from dotcoin.queries.markets import get_ticker, get_book

from tests.sources.ccxt import resources


def test_market_get_ticker(monkeypatch):
    expected = resources.PARITY_TICKER_SAMPLE
    sample = resources.MARKET_SAMPLE

    monkeypatch.setattr(fetch, "get_exchange", resources.get_exchange_mock)

    actual = get_ticker("BINANCE", sample.quote, sample.base)

    assert actual == expected


def test_market_get_book(monkeypatch):
    expected = resources.PARITY_BOOK_SAMPLE
    sample = resources.MARKET_SAMPLE

    monkeypatch.setattr(fetch, "get_exchange", resources.get_exchange_mock)

    actual = get_book("BINANCE", sample.quote, sample.base)

    assert actual == expected
