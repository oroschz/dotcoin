import ccxt

from dotcoin.core.types import Market, Book, Ticker
from dotcoin.core.abstract import Exchange
from dotcoin.sources.ccxt.exchange import CCXTExchange

from tests.sources.ccxt.resources import ExchangeMockAPI


def test_ccxt_exchange_inherits_from_abc_exchange():
    assert issubclass(CCXTExchange, Exchange)


def test_ccxt_exchange_get_markets(monkeypatch):
    monkeypatch.setattr(ccxt, "binance", ExchangeMockAPI)

    exchange = CCXTExchange("BINANCE", "binance")
    markets = exchange.markets()

    assert isinstance(markets, list)
    for market in markets:
        assert isinstance(market, Market)


def test_ccxt_exchange_has_market(monkeypatch):
    monkeypatch.setattr(ccxt, "bitfinex", ExchangeMockAPI)

    exchange = CCXTExchange("BITFINEX", "bitfinex")
    exists = exchange.has_market(Market('BTC', 'ETH'))

    assert exists is True


def test_ccxt_exchange_has_not_such_market(monkeypatch):
    monkeypatch.setattr(ccxt, "kraken", ExchangeMockAPI)

    exchange = CCXTExchange("KRAKEN", "kraken")
    exists = exchange.has_market(Market('BTC', 'LTC'))

    assert exists is False


def test_ccxt_exchange_get_ticker(monkeypatch):
    monkeypatch.setattr(ccxt, "southxchange", ExchangeMockAPI)

    exchange = CCXTExchange("SOUTHEXCHANGE", "southxchange")
    ticker = exchange.get_ticker(Market('BTC', 'ETH'))

    assert isinstance(ticker, Ticker)


def test_ccxt_exchange_get_book(monkeypatch):
    monkeypatch.setattr(ccxt, "bittrex", ExchangeMockAPI)

    exchange = CCXTExchange("BITTREX", "bittrex")
    book = exchange.get_book(Market('BTC', 'ETH'))

    assert isinstance(book, Book)
