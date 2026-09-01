"""
Utilities for working with hyperlinks.
"""

from urllib.parse import urljoin

from bs4 import BeautifulSoup
from bs4.element import Tag

from scraper.extractors.text import extract_text


def extract_href(
    element: Tag | None,
    base_url: str,
) -> str:
    """
    Extract and normalize the href attribute from an HTML element.
    """

    if element is None:
        return ""

    href = element.get("href")

    if not href:
        return ""

    return urljoin(
        base_url,
        href,
    )


def extract_link_by_text(
    soup: BeautifulSoup,
    texts: list[str],
    base_url: str,
) -> str | None:
    """
    Find an external link by matching its visible text.

    Scholarship Union links are ignored so that internal
    navigation links are not mistaken for official URLs.
    """

    normalized_texts = [
        text.strip().lower()
        for text in texts
    ]

    for link in soup.find_all("a"):

        link_text = extract_text(link).strip().lower()

        if not link_text:
            continue

        if not any(
            text in link_text
            for text in normalized_texts
        ):
            continue

        href = extract_href(
            link,
            base_url,
        )

        if not href:
            continue

        if "scholarshipunion.com" in href.lower():
            continue

        return href

    return None