from dotcoin.tables.utility import print_table

from tests.tables import resources


def test_print_ticker_table():
    expected = resources.TICKER_PRINT
    actual = print_table(resources.TICKER_TABLE)

    assert actual == expected


def test_print_book_table():
    expected = resources.BOOK_PRINT
    actual = print_table(resources.EQUITY_BOOK_TABLE_SAMPLE)

    assert actual == expected


def test_print_exchanges_table():
    expected = resources.EXCHANGES_PRINT
    actual = print_table(resources.EXCHANGES_TABLE)

    assert actual == expected


def test_print_markets_table():
    expected = resources.MARKETS_PRINT
    actual = print_table(resources.MARKETS_TABLE)

    assert actual == expected
