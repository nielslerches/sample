"""
utilities.py - Unisport Sample webservice
"""

from re import match
from money import Money

def paginate(items, page_size):
    """
    Paginates a list.

    :param items: the items to paginate.
    :param page_size: the size of each page.
    :returns: the paginated items-list, where each page is size of page_size.
    """
    pages = []
    start = 0
    end = 0
    for i in range(len(items)):
        end = i + page_size
        if i % page_size == 0:
            page = items[start:end]
            pages.append(page)
            start = end
    return pages

def parse_money(value, currency):
    """
    Parses a money-amount based on its value and currency-type.

    :param value: the value of the money-amount
    :param currency: the currency-type of the money
    :returns: Money(value, currency)
    """
    if match(r".+(\.|,)00$", value):
        return Money(value[:-3], currency)
    return Money(value, currency)