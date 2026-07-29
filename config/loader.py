"""
Utilities for loading scraper configuration files.
"""

from pathlib import Path
import yaml


class ScraperConfig:
    """
    Loads scraper configuration from YAML files.
    """

    def __init__(self, filename: str):

        config_dir = (
            Path(__file__).parent
            / "scrapers"
        )

        self.path = config_dir / filename

        with open(
            self.path,
            "r",
            encoding="utf-8",
        ) as file:

            self.data = yaml.safe_load(file)

    def get(self, *keys):

        value = self.data

        for key in keys:

            value = value[key]

        return value