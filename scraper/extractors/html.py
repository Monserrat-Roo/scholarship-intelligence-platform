"""
General HTML helper functions.
"""

from bs4 import BeautifulSoup

def create_soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(
        html,
        "html.parser",
    )