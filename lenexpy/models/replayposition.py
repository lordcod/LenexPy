from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

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


class RelayPosition(XmlRoot):
    athlete: Athlete = XmlElement(name="ATHLETE")
    athleteid: int = XmlAttribute(name="athleteid")
    meetinfo: MeetInfoEntry = XmlElement(name="MEETINFO")
    number: int = XmlAttribute(name="number", required=True)
    reaction_time: ReactionTime = XmlAttribute(name="reactiontime")
    status: StatusRelayPosition = XmlAttribute(name="status")
