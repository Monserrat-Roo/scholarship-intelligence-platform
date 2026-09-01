from scraper.base_scraper import BaseScraper
from scraper.http_client import HTTPClient
from scraper.dto.opportunity_listing import OpportunityListing

from scraper.extractors.html import create_soup
from scraper.extractors.text import extract_text
from scraper.extractors.links import extract_href

from config.loader import ScraperConfig


class ScholarshipUnionListScraper(BaseScraper):

    def __init__(self):

        self.config = ScraperConfig(
            "scholarship_union.yaml"
        )

        self.client = HTTPClient()

        self.url = self.config.get(
            "listing",
            "url",
        )

    def fetch(self):

        return self.client.get(self.url)

    def parse(self, html):

        soup = create_soup(html)

        cards = soup.select(

            self.config.get(
                "listing",
                "card_selector",
            )

        )

        opportunities = []

        for card in cards:

            link = card.select_one(

                self.config.get(
                    "listing",
                    "title_selector",
                )

            )

            if not link:
                continue

            opportunities.append(

                OpportunityListing(

                    title=extract_text(link),

                    detail_url=extract_href(
                        link,
                        self.config.get(
                            "base_url"
                        ),
                    ),
                )

            )

        return opportunities