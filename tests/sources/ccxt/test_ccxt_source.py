import ccxt
import pytest

from dotcoin.sources.ccxt import source
from dotcoin.sources.ccxt.source import CCXTSource
from dotcoin.sources.ccxt.exchange import CCXTExchange

from tests.sources.ccxt.resources import ExchangeMockAPI

MOCK_SUPPORTED = {
    'SOURCE1': 'source1',
    'SOURCE2': 'source2',
    'BINANCE': 'binance'
}


def test_ccxt_source_all_exchanges(monkeypatch):
    monkeypatch.setattr(source, 'SUPPORTED', MOCK_SUPPORTED)

    expected = ['SOURCE1', 'SOURCE2', 'BINANCE']
    actual = CCXTSource.exchanges()

    assert actual == expected


def test_ccxt_source_has_exchange(monkeypatch):
    monkeypatch.setattr(source, 'SUPPORTED', MOCK_SUPPORTED)
    has_source_2 = CCXTSource.has_exchange('SOURCE2')

    assert has_source_2 is True


def test_ccxt_source_has_not_exchange(monkeypatch):
    monkeypatch.setattr(source, 'SUPPORTED', MOCK_SUPPORTED)
    has_source_3 = CCXTSource.has_exchange('SOURCE3')

    assert has_source_3 is False


def test_ccxt_source_get_exchange(monkeypatch):
    monkeypatch.setattr(ccxt, 'binance', ExchangeMockAPI)
    monkeypatch.setattr(source, 'SUPPORTED', MOCK_SUPPORTED)

    exchange = CCXTSource.get_exchange('BINANCE')

    assert isinstance(exchange, CCXTExchange)


def test_ccxt_source_get_not_supported_exchange(monkeypatch):
    monkeypatch.setattr(source, 'SUPPORTED', MOCK_SUPPORTED)
    with pytest.raises(KeyError):
        CCXTSource.get_exchange('SOURCE3')
