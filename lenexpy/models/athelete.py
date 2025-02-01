from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.club import Club
from lenexpy.models.entry import Entry
from lenexpy.models.gender import Gender
from lenexpy.models.handicap import Handicap
from lenexpy.models.nation import Nation
from lenexpy.models.result import Result


class Athlete(XmlRoot):
    athleteid: int = XmlAttribute(name="athleteid", required=True)
    birthdate: LocalDate = XmlAttribute(name="birthdate", required=True)
    club: Club = XmlElement(name="CLUB")
    entries: List[Entry] = XmlElement(name="ENTRY")
    firstname: str = XmlAttribute(name="firstname", required=True)
    firstnameEn: str = XmlAttribute(name="firstname.en")
    gender: Gender = XmlAttribute(name="gender", required=True)
    handicap: Handicap = XmlElement(name="HANDICAP")
    lastname: str = XmlAttribute(name="lastname", required=True)
    lastnameEn: str = XmlAttribute(name="lastname.en")
    level: str = XmlAttribute(name="level")
    license: str = XmlAttribute(name="license")
    nameprefix: str = XmlAttribute(name="nameprefix")
    nation: Nation = XmlAttribute(name="nation")
    passport: str = XmlAttribute(name="passport")
    results: List[Result] = XmlElementWrapper("RESULTS", "RESULT")
    swrid: int = XmlAttribute(name="swrid")
