# Scraper Framework

Every scraper in the project follows the same workflow:

1. Fetch the webpage.
2. Parse the HTML.
3. Extract information.
4. Transform it into `OpportunityRecord`.
5. Return a list of normalized opportunities.

All scraper implementations inherit from `BaseScraper`.