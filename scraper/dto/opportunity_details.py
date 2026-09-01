"""
Represents the complete information extracted
from a scholarship opportunity detail page.
"""

from dataclasses import dataclass
from datetime import date


@dataclass(slots=True)
class OpportunityDetails:

    title: str

    opportunity_type: str | None = None

    organization: str | None = None

    country: str | None = None

    field: str | None = None

    status: str | None = None

    application_open_date: date | None = None

    application_deadline: date | None = None

    funding_type: str | None = None

    benefits: str | None = None

    eligibility_criteria: str | None = None

    requirements: str | None = None

    official_url: str | None = None