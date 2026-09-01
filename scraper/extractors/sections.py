"""
Utilities for extracting content sections.
"""

from bs4 import BeautifulSoup
from bs4.element import Tag

from scraper.extractors.text import extract_text


def extract_section(
    soup: BeautifulSoup,
    headings: list[str],
) -> str:
    """
    Returns the text contained in the section that starts
    with one of the given headings.
    """

    headers = soup.find_all(["h2", "h3", "h4"])

    for header in headers:

        title = extract_text(header).lower()

        if any(
            option.lower() in title
            for option in headings
        ):

            content = []

            node = header.find_next_sibling()

            while node:

                if (
                    isinstance(node, Tag)
                    and node.name in ["h2", "h3", "h4"]
                ):
                    break

                content.append(
                    extract_text(node)
                )

                node = node.find_next_sibling()

            return "\n".join(
                line
                for line in content
                if line
            )

    return ""

def extract_labeled_value(
    soup: BeautifulSoup,
    label: str,
) -> str:
    """
    Extracts the value associated with a labeled <dt> element.

    Example:

        <dt>Deadline</dt>
        <dd>7 September 2026</dd>

    Parameters
    ----------
    soup : BeautifulSoup
        Parsed HTML document.

    label : str
        Label to search for.

    Returns
    -------
    str
        Associated text value, or an empty string if not found.
    """

    labels = soup.find_all("dt")

    for element in labels:

        if extract_text(element).strip().lower() == label.lower():

            value = element.find_next_sibling("dd")

            if value is not None:
                return extract_text(value)

    return ""