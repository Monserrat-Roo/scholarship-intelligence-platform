from datetime import date

from bs4 import BeautifulSoup

from scraper.extractors.dates import (
    extract_deadline,
)


def test_extract_deadline_from_json_ld():

    html = """
    <html>
        <head>
            <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@type": "Event",
                "applicationDeadline": "2026-10-01"
            }
            </script>
        </head>
    </html>
    """

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    result = extract_deadline(
        soup
    )

    assert result == date(
        2026,
        10,
        1,
    )


def test_extract_deadline_from_visible_text():

    html = """
    <html>
        <body>
            <p>
                Deadline 7 September 2026
            </p>
        </body>
    </html>
    """

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    result = extract_deadline(
        soup
    )

    assert result == date(
        2026,
        9,
        7,
    )


def test_extract_deadline_returns_none():

    html = """
    <html>
        <body>
            <p>
                No deadline available.
            </p>
        </body>
    </html>
    """

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    result = extract_deadline(
        soup
    )

    assert result is None