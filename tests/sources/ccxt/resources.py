import ccxt
from typing import List

from dotcoin.core.types import Market, Context, Ticker, Order, Book
from dotcoin.core.abstract import Exchange

SYMBOL_SAMPLE = 'ETH/BTC'

MARKET_SAMPLE = Market("BTC", "ETH")

CONTEXT_SAMPLE = Context(MARKET_SAMPLE, "BINANCE")

SOURCE_TICKER_SAMPLE = {
    'symbol': 'ETH/BTC', 'timestamp': 1584330712574, 'datetime': '2020-03-16T03:51:52.574Z',
    'high': 0.023629,
    'low': 0.022214, 'bid': 0.023176, 'bidVolume': 0.086, 'ask': 0.023184, 'askVolume': 4.0,
    'vwap': 0.02317318,
    'open': 0.023344, 'close': 0.023182, 'last': 0.023182, 'previousClose': 0.02334,
    'change': -0.000162,
    'percentage': -0.694, 'average': None, 'baseVolume': 336552.631,
    'quoteVolume': 7798.99618515,
    'info': {
        'symbol': 'ETHBTC', 'priceChange': '-0.00016200', 'priceChangePercent': '-0.694',
        'weightedAvgPrice': '0.02317318', 'prevClosePrice': '0.02334000',
        'lastPrice': '0.02318200',
        'lastQty': '1.16200000', 'bidPrice': '0.02317600', 'bidQty': '0.08600000',
        'askPrice': '0.02318400',
        'askQty': '4.00000000', 'openPrice': '0.02334400', 'highPrice': '0.02362900',
        'lowPrice': '0.02221400',
        'volume': '336552.63100000', 'quoteVolume': '7798.99618515',
        'openTime': 1584244312574,
        'closeTime': 1584330712574, 'firstId': 168500958, 'lastId': 168661713,
        'count': 160756
    }
}

PARITY_TICKER_SAMPLE = Ticker(CONTEXT_SAMPLE, **{
    'bid': 0.023176,
    'ask': 0.023184,
    'last': 0.023182,
    'volume': 336552.631,
    'var': -0.694
})

SOURCE_BOOK_SAMPLE = {
    'bids': [
        [0.02309, 10.729],
        [0.023089, 17.176],
        [0.023088, 0.121],
        [0.023086, 12.988]
    ],
    'asks': [
        [0.023094, 0.159],
        [0.0231, 4.803],
        [0.023101, 0.024],
        [0.023102, 4.0],
        [0.023103, 1.401]
    ],
    'datetime': None, 'nonce': 1087573148
}

PARITY_BOOK_SAMPLE = Book(CONTEXT_SAMPLE, bids=[
    Order(price=0.02309, base=10.729, quote=0.24773260999999996),
    Order(price=0.023089, base=17.176, quote=0.3965766639999999),
    Order(price=0.023088, base=0.121, quote=0.002793648),
    Order(price=0.023086, base=12.988, quote=0.299840968),
], asks=[
    Order(price=0.023094, base=0.159, quote=0.003671946),
    Order(price=0.0231, base=4.803, quote=0.11094929999999999),
    Order(price=0.023101, base=0.024, quote=0.000554424),
    Order(price=0.023102, base=4.0, quote=0.092408),
    Order(price=0.023103, base=1.401, quote=0.032367303),
])

SOURCE_EMPTY_BOOK_SAMPLE = {'bids': [], 'asks': [], 'datetime': None, 'nonce': 1087573148}

PARITY_EMPTY_BOOK_SAMPLE = Book(CONTEXT_SAMPLE, [], [])


class ExchangeMockAPI(ccxt.Exchange):

    def load_markets(self, *args, **kwargs):
        self.markets = {"ETH/BTC": ""}

    def fetch_ticker(self, *args, **kwargs):
        return SOURCE_TICKER_SAMPLE

    def fetch_l2_order_book(self, *args, **kwargs):
        return SOURCE_BOOK_SAMPLE


class ExchangeMock(Exchange):
    def __init__(self, *args):
        pass

    def markets(self) -> List[Market]:
        pass

    def has_market(self, market: Market) -> bool:
        return market == MARKET_SAMPLE

    def get_ticker(self, market: Market) -> Ticker:
        return PARITY_TICKER_SAMPLE

    def get_book(self, market: Market) -> Book:
        return PARITY_BOOK_SAMPLE


def get_exchange_mock(*_):
    return ExchangeMock()
