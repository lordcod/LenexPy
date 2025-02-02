from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper
from datetime import time as dtime
from .entry import Entry
from .gender import Gender
from .handicap import Handicap
from .nation import Nation
from .result import Result


class Athlete(XmlRoot):
    athleteid: int = XmlAttribute(name="athleteid", required=True)
    birthdate: dtime = XmlAttribute(name="birthdate", required=True)
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
