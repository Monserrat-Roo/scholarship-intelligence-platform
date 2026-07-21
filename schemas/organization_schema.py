from dataclasses import dataclass

@dataclass
class OrganizationRecord:
    name: str
    country: str | None = None
    website: str | None = None
