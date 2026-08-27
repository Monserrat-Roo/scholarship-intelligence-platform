"""
Scraper for Scholarship Union opportunity detail pages.
"""

from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper
from scraper.http_client import HTTPClient

from scraper.extractors.html import create_soup
from scraper.extractors.text import extract_text
from scraper.extractors.sections import extract_section
from scraper.extractors.dates import extract_date
from scraper.dto.opportunity_details import OpportunityDetails

class ScholarshipUnionDetailScraper(BaseScraper):

    def __init__(self, url):

        self.url = url

        self.client = HTTPClient()

    def fetch(self):

        return self.client.get(self.url)

    def parse(self, html):

        soup = create_soup(html)

        title = extract_text(
            soup.select_one(
                self.config.get(
                    "detail",
                    "title_selector"
                )
            )
        )

        deadline = extract_date(
            soup,
            self.config.get(
                "detail",
                "deadline_selector"
            ),
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

        return OpportunityDetails(

            title=title,

            application_deadline=deadline,

            benefits=benefits,

            eligibility_criteria=eligibility,

            requirements=requirements,
        )
    
    def scrape(self):

        html = self.fetch()

        return self.parse(html)