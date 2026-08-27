"""
Mapper for Scholarship Union.

Transforms parsed HTML into OpportunityRecord.
"""

"""
Transforms temporary scraping objects
into OpportunityRecord.
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

            source="Scholarship Union",

            source_url=listing.detail_url,

            organization=details.organization,

            opportunity_type="scholarship",

            benefits=details.benefits,

            eligibility_criteria=details.eligibility_criteria,

            requirements=details.requirements,

            application_deadline=details.application_deadline,

            official_url=details.official_url,
        )