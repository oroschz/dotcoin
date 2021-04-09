from dotcoin.tables.book import table_book
from dotcoin.tables.ticker import table_ticker

from tests.tables import resources


def test_table_content_ticker():
    expected = resources.TICKER_TABLE

    ticker = resources.TICKER
    actual = table_ticker(ticker)

    assert actual == expected


def test_table_content_book():
    expected = resources.EQUITY_BOOK_TABLE_SAMPLE

    book = resources.BOOK
    content = table_book(book)

    assert content == expected
