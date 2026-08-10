"""
Utilities for parsing dates.
"""

from datetime import datetime
from datetime import date

def parse_date(
    value: str,
) -> date | None:

    if not value:
        return None

    formats = [

        "%d %B %Y",

        "%B %d, %Y",

        "%Y-%m-%d",

    ]
    
    for fmt in formats:

        try:

            return datetime.strptime(
                value,
                fmt,
            ).date()

        except ValueError:

            pass

    return None