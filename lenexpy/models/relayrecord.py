from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from .replayposition import RelayPosition
from lenexpy.models.club import Club
from lenexpy.models.reactiontime import ReactionTime
from .contact import Contact
from .gender import Gender
from .athelete import Athlete
from .meetinfoentry import MeetInfoEntry
from .agegroup import AgeGroup
from .course import Course
from .record import Record


class StatusRelayPosition(StrEnum):
    DSQ = 'DSQ'
    DNF = 'DNF'


class RelayRecord(XmlRoot):
    club: Club = XmlElement(name="CLUB")
    name: str = XmlAttribute(name="name")
    relayPositions: List[RelayPosition] = XmlElementWrapper("RELAYPOSITIONS", "RELAYPOSITION")
