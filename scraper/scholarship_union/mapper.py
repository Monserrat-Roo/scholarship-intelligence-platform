"""
Mapper for Scholarship Union.

Transforms parsed HTML into OpportunityRecord.
"""

from models.opportunity import OpportunityRecord

from scraper.dto.opportunity_listing import OpportunityListing
from scraper.dto.opportunity_details import OpportunityDetails


class OpportunityMapper:

    @staticmethod
    def build(
        listing: OpportunityListing,
        details: OpportunityDetails,
    ) -> OpportunityRecord:

        return OpportunityRecord(

            title=listing.title,

            opportunity_type=(
                details.opportunity_type
                or "unknown"
            ),

            source="Scholarship Union",

            source_url=listing.detail_url,

            organization=details.organization,

            country=details.country,

            field=details.field,

            status=details.status,

            application_open_date=(
                details.application_open_date
            ),

            application_deadline=(
                details.application_deadline
            ),

            funding_type=details.funding_type,

            benefits=details.benefits,

            eligibility_criteria=(
                details.eligibility_criteria
            ),

            requirements=details.requirements,

            official_url=details.official_url,
        )