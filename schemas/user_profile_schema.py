from dataclasses import dataclass

@dataclass
class UserProfile:
    preferred_degrees: list[str]
    preferred_countries: list[str]
    preferred_fields: list[str]
    english_level: str
    gpa: float | None = None