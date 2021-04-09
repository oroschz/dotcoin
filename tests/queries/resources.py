from typing import List

from dotcoin.core.types import Market, Book, Ticker
from dotcoin.core.abstract import Exchange

MARKETS = {
    'EXCHANGE1': [
        Market('BTC', 'ETH'),
        Market('BTC', 'LTC')
    ],
    'EXCHANGE2': [
        Market('BTC', 'ETH'),
        Market('USDT', 'BTC')
    ],
    'EXCHANGE3': [
        Market('USDT', 'BTC'),
    ],
    'EXCHANGE4': [
        Market('USDT', 'BTC'),
        Market('BTC', 'ETH'),
        Market('BTC', 'LTC')
    ]
}


class MockExchange(Exchange):
    def __init__(self, exchange):
        self.name = exchange

    def markets(self) -> List[Market]:
        return MARKETS[self.name]

    def has_market(self, market: Market) -> bool:
        return market in MARKETS[self.name]

    def get_ticker(self, market: Market) -> Ticker:
        pass

    def get_book(self, market: Market) -> Book:
        pass


def all_mock_exchanges():
    names = MARKETS.keys()
    return [MockExchange(name) for name in names]


def get_mock_exchange(name: str):
    return MockExchange(name)


def all_mock_markets():
    markets = set()
    for local in MARKETS.values():
        markets.update(local)
    return markets
