"""
Domain model representing an academic opportunity.

This model is the central object of the Scholarship Intelligence Platform.
Every scraper must transform the extracted information into an OpportunityRecord
before sending it to the ETL pipeline.
"""

from dataclasses import dataclass
from datetime import date

@dataclass
class OpportunityRecord:
    """
    Represents a normalized academic opportunity.
    Every opportunity collected from any source should be transformed into
    this format before being processed by the ETL pipeline.
    """

    title: str
    opportunity_type: str

    organization: str | None = None

    country: str | None = None

    field: str | None = None

    status: str | None = None
    application_open_date: date | None = None
    application_deadline: date | None = None

    funding_type: str | None = None
    benefits: str | None = None

    elegibility_criteria: str | None = None
    requirements: str | None = None

    source: str = ""
    source_url: str = ""
    official_url: str | None = None