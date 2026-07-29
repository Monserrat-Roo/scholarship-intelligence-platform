"""
Utilities for working with hyperlinks.
"""

from urllib.parse import urljoin
from bs4.element import Tag

def extratc_href(
    element: Tag | None, 
    base_url: str, 
) -> str:
    if element is None:
        return ""
        
    href = element.get("href")
    if not href:
        return ""

    return urljoin(
        base_url,
        href
    )