"""
Scraper for Scholarship Union listing pages.
"""

from bs4 import BeautifulSoup

from scraper.base_scraper import BaseScraper

from scraper.http_client import HTTPClient

from scraper.dto.opportunity_listing import OpportunityListing


class ScholarshipUnionListScraper(BaseScraper):

    def __init__(self, url: str):

        self.url = url

        self.client = HTTPClient()

    def fetch(self):

        return self.client.get(self.url)

    def parse(self, html):

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        opportunities = []

        cards = soup.select(
            "article.up-listing-card"
        )

        for card in cards:

            link = card.select_one("h3 a")

            if not link:
                continue

            opportunities.append(

                OpportunityListing(

                    title=link.text.strip(),

                    detail_url=link.get("href")
                )

            )

        return opportunities