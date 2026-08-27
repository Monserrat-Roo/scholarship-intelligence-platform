"""
Utilities for parsing dates.
"""

from datetime import date, datetime

from scraper.extractors.text import extract_text


def parse_date(value: str) -> date | None:
    """
    Convert a textual date into a Python date object.
    """

    if not value:
        return None

    value = value.strip()

    formats = [
        "%d %B %Y",
        "%B %d, %Y",
        "%d %b %Y",
        "%b %d, %Y",
        "%Y-%m-%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(
                value,
                fmt,
            ).date()
        except ValueError:
            continue

    return None


def extract_date(
    soup,
    selector: str,
) -> date | None:
    """
    Extract a date from an HTML element.
    """

    element = soup.select_one(selector)

    if element is None:
        return None

    value = element.get("datetime")

    if not value:
        value = extract_text(element)

    return parse_date(value)