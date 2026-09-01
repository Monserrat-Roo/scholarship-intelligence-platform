"""
Run the Scholarship Union scraping pipeline.
"""

from scraper.scholarship_union.list_scraper import (
    ScholarshipUnionListScraper,
)

from scraper.scholarship_union.detail_scraper import (
    ScholarshipUnionDetailScraper,
)

from scraper.scholarship_union.mapper import (
    OpportunityMapper,
)


def main():

    print("=" * 60)
    print("Scholarship Intelligence Platform")
    print("=" * 60)

    print("\nSource: Scholarship Union")

    # --------------------------------------------------
    # 1. Scrape listing page
    # --------------------------------------------------

    list_scraper = ScholarshipUnionListScraper()

    listings = list_scraper.scrape()

    print(
        f"\nOpportunities found: {len(listings)}"
    )

    if not listings:
        print("No opportunities found.")
        return

    # --------------------------------------------------
    # 2. Process detail pages
    # --------------------------------------------------

    records = []

    for index, listing in enumerate(
        listings,
        start=1,
    ):

        print(
            f"\n[{index}/{len(listings)}]"
        )

        print(
            f"Title: {listing.title}"
        )

        print(
            f"URL: {listing.detail_url}"
        )

        try:

            detail_scraper = (
                ScholarshipUnionDetailScraper(
                    listing.detail_url
                )
            )

            details = detail_scraper.scrape()

            record = OpportunityMapper.build(
                listing,
                details,
            )

            records.append(record)

            print("✓ Processed")

        except Exception as error:

            print(
                f"✗ Error: {error}"
            )

    # --------------------------------------------------
    # 3. Summary
    # --------------------------------------------------

    print("\n" + "=" * 60)

    print(
        f"Listings found: {len(listings)}"
    )

    print(
        f"Records created: {len(records)}"
    )

    print("=" * 60)

    # --------------------------------------------------
    # 4. Preview
    # --------------------------------------------------

    for record in records[:3]:

        print("\nOpportunityRecord")
        print("-" * 40)

        print(
            f"Title: {record.title}"
        )

        print(
            f"Type: {record.opportunity_type}"
        )

        print(
            f"Source: {record.source}"
        )

        print(
            f"Deadline: {record.application_deadline}"
        )

        print(
            f"Official URL: {record.official_url}"
        )


if __name__ == "__main__":
    main()