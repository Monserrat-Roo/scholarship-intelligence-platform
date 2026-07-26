"""
Scraper for Scholarship Union opportunity detail pages.
"""

from bs4 import BeautifulSoup

from scraper.base_scraper import BaseScraper

from scraper.http_client import HTTPClient

from scraper.dto.opportunity_details import OpportunityDetails


class ScholarshipUnionDetailScraper(BaseScraper):

    def __init__(self, url):

        self.url = url

        self.client = HTTPClient()

    def fetch(self):

        return self.client.get(self.url)

    def parse(self, html):

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        return OpportunityDetails(
            title=""
        )