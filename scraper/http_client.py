"""
HTTP client used by all scrapers.
This module centralizes HTTP requests so that every scraper 
shares the same timeout, headers and error handling. 
"""

from __future__ import annotations
import requests

class HTTPClient:
    """Simple HTTP client for downloading web pages."""
    DEFAULT_TIMEOUT = 30
    DEFAULT_HEADERS = {
        "User-Agent": (
            "Schoolarship-Intelligence-Platform/0.1"
            "(Educational Project)"
        )
    }

    def get(self, url: str) -> str:
        """
        Download a webpage.

        Parameters
        ----------
        url : str
            Webpage URL.

        Returns
        -------
        str
            HTML content.
        """

        response = requests.get(
            url,
            headers=self.DEFAULT_HEADERS,
            timeout=self.DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        return response.text
