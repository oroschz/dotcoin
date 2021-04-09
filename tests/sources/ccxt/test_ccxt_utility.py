import pytest

from dotcoin.sources.ccxt.utility import symbol_to_market, parse_ticker, parse_order, parse_book

from tests.sources.ccxt import resources


def test_ccxt_parse_symbol():
    received = resources.SYMBOL_SAMPLE
    expected = resources.MARKET_SAMPLE

    actual = symbol_to_market(received)

    assert actual == expected


def test_ccxt_parse_empty_symbol():
    with pytest.raises(ValueError):
        symbol_to_market('')


def test_ccxt_parse_unexpected_symbol():
    with pytest.raises(ValueError):
        symbol_to_market('BTC_ETH')


def test_ccxt_parse_ticker():
    received = resources.SOURCE_TICKER_SAMPLE
    expected = resources.PARITY_TICKER_SAMPLE

    actual = parse_ticker(resources.CONTEXT_SAMPLE, received)

    assert actual == expected


def test_ccxt_parse_void_ticker():
    with pytest.raises(KeyError):
        parse_ticker(resources.CONTEXT_SAMPLE, {})


def test_ccxt_parse_ticker_with_invalid_data():
    received = resources.SOURCE_TICKER_SAMPLE
    received.update({'bid': None})
    with pytest.raises(TypeError):
        parse_ticker(resources.CONTEXT_SAMPLE, received)


def test_ccxt_parse_order():
    received = resources.SOURCE_BOOK_SAMPLE['bids'][0]
    expected = resources.PARITY_BOOK_SAMPLE.bids[0]

    actual = parse_order(received)

    assert actual == expected


def test_ccxt_parse_empty_order():
    with pytest.raises(ValueError):
        parse_order([])


def test_ccxt_parse_invalid_order():
    with pytest.raises(TypeError):
        parse_order(['0.023165', '0.536'])


def test_ccxt_parse_book():
    received = resources.SOURCE_BOOK_SAMPLE
    expected = resources.PARITY_BOOK_SAMPLE

    actual = parse_book(resources.CONTEXT_SAMPLE, received)

    assert actual == expected


def test_ccxt_parse_emtpy_book():
    received = resources.SOURCE_EMPTY_BOOK_SAMPLE
    expected = resources.PARITY_EMPTY_BOOK_SAMPLE

    actual = parse_book(resources.CONTEXT_SAMPLE, received)

    assert actual == expected


def test_ccxt_parse_void_book():
    with pytest.raises(KeyError):
        parse_book(resources.CONTEXT_SAMPLE, {})
