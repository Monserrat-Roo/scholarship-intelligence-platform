"""
Scraper for Scholarship Union opportunity detail pages.
"""

from bs4 import BeautifulSoup

from scraper.base_scraper import BaseScraper
from scraper.http_client import HTTPClient

from scraper.extractors.html import create_soup
from scraper.extractors.text import extract_text
from scraper.extractors.sections import extract_section
from scraper.extractors.dates import extract_deadline
from scraper.extractors.links import extract_link_by_text

from scraper.dto.opportunity_details import OpportunityDetails

from config.loader import ScraperConfig


class ScholarshipUnionDetailScraper(BaseScraper):

    def __init__(self, url: str):

        self.url = url

        self.client = HTTPClient()

        self.config = ScraperConfig(
            "scholarship_union.yaml"
        )

    def fetch(self) -> str:

        return self.client.get(
            self.url
        )

    def detect_opportunity_type(
        self,
        soup: BeautifulSoup,
    ) -> str | None:
        """
        Detect the type of opportunity.

        The scraper first checks configured
        opportunity type keywords in the page title.
        """

        title = extract_text(
            soup.select_one(
                self.config.get(
                    "detail",
                    "title_selector",
                )
            )
        ).lower()

        opportunity_types = self.config.get(
            "opportunity_types"
        )

        for opportunity_type, keywords in opportunity_types.items():

            for keyword in keywords:

                if keyword.lower() in title:

                    return opportunity_type

        return None

    def parse(
        self,
        html: str,
    ) -> OpportunityDetails:

        soup = create_soup(html)

        title = extract_text(
            soup.select_one(
                self.config.get(
                    "detail",
                    "title_selector",
                )
            )
        )

        opportunity_type = (
            self.detect_opportunity_type(
                soup
            )
        )

        deadline = extract_deadline(
            soup
        )

        benefits = extract_section(
            soup,
            self.config.get(
                "sections",
                "benefits",
            ),
        )

        eligibility = extract_section(
            soup,
            self.config.get(
                "sections",
                "eligibility",
            ),
        )

        requirements = extract_section(
            soup,
            self.config.get(
                "sections",
                "requirements",
            ),
        )

        official_url = extract_link_by_text(
            soup,
            self.config.get(
                "detail",
                "official_link_text",
            ),
            self.config.get(
                "base_url",
            ),
        )

        return OpportunityDetails(

            title=title,

            opportunity_type=opportunity_type,

            application_deadline=deadline,

            benefits=benefits,

            eligibility_criteria=eligibility,

            requirements=requirements,

            official_url=official_url,
        )

    def scrape(self):

        html = self.fetch()

        return self.parse(
            html
        )