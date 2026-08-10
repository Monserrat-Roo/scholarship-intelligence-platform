"""
Utilities for extracting content sections.
"""

from bs4 import BeautifulSoup

def find_section(
    soup: BeautifulSoup,
    heading: str,
):

    headers = soup.find_all(
        ["h2", "h3", "h4"]
    )

    for header in headers:
        if heading.lower() in header.text.lower()
            return header

    return None