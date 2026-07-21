from dataclasses import dataclass
from typing import Optional

@dataclass
class Scolarship:

    #Identification 
    title: str
    source: str
    source_url: str
    official_url: Optional[str]

    #Organization
    university: Optional[str]
    organization: Optional[str]

    #Location
    country: Optional[str]
    city: Optional[str]

    #Studies
    degree_level: Optional[str]
    field: Optional[str]
    durarion: Optional[str]

    #Financing
    fully_funded: Optional[bool]
    tuition: Optional[bool]
    monthly_stipend: Optional[bool]
    housing: Optional[bool]
    insurance: Optional[bool]
    travel_allowance: Optional[bool]

    #Requirements
    ielts: Optional[bool]
    toefl: Optional[bool]
    gre: Optional[bool]
    work_experience: Optional[bool]

    recommendation_letters: Optional[int]
    motivation_letter: Optional[bool]
    cv_required: Optional[bool]

    #Dates
    deadline: Optional[str]
    published_date: Optional[str]

    #Description
    description: Optional[str]
    benefits: Optional[str]
    elegibility: Optional[str]
    application_process: Optional[str]