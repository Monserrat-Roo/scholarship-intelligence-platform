"""
Scraper for Scholarship Union listing pages.
"""

from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper
from scraper.http_client import HTTPClient

class ScholarshipUnionListScraper(BaseScraper):
    def __init__(self, url: str):
        self.url = url
        self.client = HTTPClient()

    def fetch(self) -> str:
        return self.client.get(self.url)

    def parse(self, html: str):
        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        cards = soup.select(
            "article.up-listing-card"
        )

        return cards