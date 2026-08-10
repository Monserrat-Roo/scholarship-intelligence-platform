from scraper.scholarship_union.list_scraper import (
    ScholarshipUnionListScraper,
)


def test_list_scraper_creation():

    scraper = ScholarshipUnionListScraper()

    assert scraper.url.startswith(
        "https://"
    )