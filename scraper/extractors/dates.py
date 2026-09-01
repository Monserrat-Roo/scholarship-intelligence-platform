"""
Utilities for extracting application deadlines from HTML.
"""

import json
import re
from datetime import date, datetime

from bs4 import BeautifulSoup
from bs4.element import Tag


def parse_date(value: str | None) -> date | None:
    """
    Convert a date string into a datetime.date object.

    Supports ISO dates and common date formats.
    """

    if not value:
        return None

    value = value.strip()

    # ISO format: 2026-10-01
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        pass

    formats = [
        "%d %B %Y",
        "%d %b %Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(
                value,
                fmt,
            ).date()
        except ValueError:
            continue

    return None


def extract_json_ld_deadline(
    soup: BeautifulSoup,
) -> date | None:
    """
    Extract applicationDeadline from JSON-LD structured data.
    """

    scripts = soup.find_all(
        "script",
        type="application/ld+json",
    )

    for script in scripts:

        if not script.string:
            continue

        try:
            data = json.loads(script.string)
        except json.JSONDecodeError:
            continue

        objects = data if isinstance(data, list) else [data]

        for obj in objects:

            if not isinstance(obj, dict):
                continue

            deadline = obj.get(
                "applicationDeadline"
            )

            parsed = parse_date(deadline)

            if parsed:
                return parsed

    return None


def extract_deadline_from_text(
    soup: BeautifulSoup,
) -> date | None:
    """
    Search visible page text for an application deadline.
    """

    text = soup.get_text(
        separator=" ",
        strip=True,
    )

    patterns = [
        r"Deadline\s+(\d{1,2}\s+\w+\s+\d{4})",
        r"Deadline\s*[:\-]?\s*(\d{1,2}\s+\w+\s+\d{4})",
        r"closing date\s+(?:is\s+)?\w+,\s*(\d{1,2}\s+\w+\s+\d{4})",
        r"closing date\s+(?:is\s+)?(\d{1,2}\s+\w+\s+\d{4})",
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            flags=re.IGNORECASE,
        )

        if match:

            parsed = parse_date(
                match.group(1)
            )

            if parsed:
                return parsed

    return None


def extract_deadline(
    soup: BeautifulSoup,
) -> date | None:
    """
    Extract an application deadline using
    multiple fallback strategies.

    Priority:
    1. JSON-LD applicationDeadline
    2. Visible deadline text
    """

    deadline = extract_json_ld_deadline(
        soup
    )

    if deadline:
        return deadline

    return extract_deadline_from_text(
        soup
    )