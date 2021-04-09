from dotcoin.core.types import Market
from dotcoin.queries import common
from dotcoin.queries import utility
from dotcoin.queries.common import common_markets, common_exchanges

from tests.queries.resources import all_mock_exchanges, get_mock_exchange


def test_common_exchanges(monkeypatch):
    monkeypatch.setattr(common, 'all_exchanges', all_mock_exchanges)

    expected = ['EXCHANGE2', 'EXCHANGE3', 'EXCHANGE4']
    actual = common_exchanges('USDT', 'BTC')

    assert actual == expected


def test_common_markets(monkeypatch):
    monkeypatch.setattr(utility, 'get_exchange', get_mock_exchange)

    expected = [Market('BTC', 'ETH'), Market('BTC', 'LTC')]
    actual = common_markets(['EXCHANGE1', 'EXCHANGE4'])

    assert actual == expected
