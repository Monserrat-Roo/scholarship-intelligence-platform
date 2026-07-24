"""
Base class for all opportunity scrapers.

Every scraper must inherit from BaseScraper and implement
its abstract methods.
"""
from abc import ABC, abstractmethod
from models.opportunity import OpportunityRecord

class BaseScraper(ABC):
    """
    Abstract base class for all scrapers.
    """

    @abstractmethod
    def fetch(self) -> str:
        """
        Download the webpage.

        Returns
        -------
        str
            HTML content.
        """
        pass

    @abstractmethod
    def parse(
        self,
        html: str
    ) -> list[OpportunityRecord]:
        """
        Parse HTML and return opportunities.
        """
        pass

    def scrape(self) -> list[OpportunityRecord]:
        """
        Complete scraping workflow.
        """

        html = self.fetch()

        opportunities = self.parse(html)

        return opportunities