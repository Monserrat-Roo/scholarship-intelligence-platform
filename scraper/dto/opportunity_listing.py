 """
Represents a scholarship card extracted from a listing page.
"""

from dataclasses import dataclass

@dataclass(slots=True)
class OpportunityListing:
    """
    Minimal information obtained from a listing page.

    This object is later enriched by the detail scraper.
    """

    title: str
    detail_url: str