from pathlib import Path

from scraper.scholarship_union.list_scraper import (
    ScholarshipUnionListScraper,
)


FIXTURES = Path(
    "tests/fixtures/scholarship_union"
)


def test_listing_page_returns_opportunities():

    html = (
        FIXTURES
        / "listing_page_1.html"
    ).read_text(
        encoding="utf-8"
    )

    scraper = ScholarshipUnionListScraper()

    results = scraper.parse(html)

    assert len(results) > 0


def test_listing_contains_valid_urls():

    html = (
        FIXTURES
        / "listing_page_1.html"
    ).read_text(
        encoding="utf-8"
    )

    scraper = ScholarshipUnionListScraper()

    results = scraper.parse(html)

    for result in results:

        assert result.title

        assert result.detail_url.startswith(
            "https://scholarshipunion.com"
        )