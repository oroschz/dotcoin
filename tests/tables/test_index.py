from dotcoin.tables.index import table_exchanges, table_markets
from tests.tables import resources


def test_table_content_exchanges():
    expected = resources.EXCHANGES_TABLE

    actual = table_exchanges(resources.EXCHANGES)

    assert actual == expected


def test_table_content_markets():
    expected = resources.MARKETS_TABLE

    actual = table_markets(resources.MARKETS, compact=True)

    assert actual == expected
