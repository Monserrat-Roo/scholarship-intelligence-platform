"""
Utility functions for extracting text from HTML.
"""

from bs4 import BeautifulSoup
from bs4.element import Tag

def extract_text(
    element: Tag | None,
    default: str ="",
) -> str:
    """
    Extract clean text from an HTML element.
    """
    if element is None: 
        return default

    return element.get_text(
        separator=" ",
        strip=True
    )
