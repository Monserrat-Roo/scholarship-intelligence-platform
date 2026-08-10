from abc import ABC
from abc import abstractmethod

from models.opportunity import OpportunityRecord


class BaseScraper(ABC):

    @abstractmethod
    def fetch(self) -> str:
        ...

    @abstractmethod
    def parse(
        self,
        html: str,
    ):
        ...

    def scrape(self):

        html = self.fetch()

        return self.parse(html)