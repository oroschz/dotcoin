from dotcoin.core.types import Market
from dotcoin.queries import index
from dotcoin.queries.index import index_exchanges, index_markets, index_markets_from

from tests.queries.resources import all_mock_exchanges, get_mock_exchange, all_mock_markets


def test_index_exchanges(monkeypatch):
    monkeypatch.setattr(index, 'all_exchanges', all_mock_exchanges)

    expected = ['EXCHANGE1', 'EXCHANGE2', 'EXCHANGE3', 'EXCHANGE4']
    actual = index_exchanges()

    assert actual == expected


def test_index_markets(monkeypatch):
    monkeypatch.setattr(index, 'all_markets', all_mock_markets)

    expected = [Market('BTC', 'ETH'), Market('BTC', 'LTC'), Market('USDT', 'BTC')]
    actual = index_markets()

    assert actual == expected


def test_index_markets_from(monkeypatch):
    monkeypatch.setattr(index, 'get_exchange', get_mock_exchange)

    expected = [Market('BTC', 'ETH'), Market('USDT', 'BTC')]
    actual = index_markets_from('EXCHANGE2')

    assert actual == expected
