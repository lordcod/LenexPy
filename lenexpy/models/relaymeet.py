from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.result import Result

from .entry import Entry
from .contact import Contact
from .gender import Gender
from .athelete import Athlete
from .meetinfoentry import MeetInfoEntry


class RelayMeet(XmlRoot):
    agemax: int = XmlAttribute(name="agemax", required=True)
    agemin: int = XmlAttribute(name="agemin", required=True)
    agetotalmax: int = XmlAttribute(name="agetotalmax", required=True)
    agetotalmin: int = XmlAttribute(name="agetotalmin", required=True)
    entries: List[Entry] = XmlElementWrapper("ENTRIES", "ENTRY")
    gender: Gender = XmlAttribute(name="gender", required=True)
    handicap: int = XmlAttribute(name="handicap")
    name: str = XmlAttribute(name="name")
    number: int = XmlAttribute(name="number")
    results: List[Result] = XmlElementWrapper("RESULTS", "RESULT")
