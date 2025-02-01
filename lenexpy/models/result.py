from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.split import Split
from lenexpy.models.swimtime import SwimTime

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


class StatusResult(StrEnum):
    EXH = "EXH"
    DSQ = "DSQ"
    DNS = "DNS"
    DNF = "DNF"
    SICK = "SICK"
    WDR = "WDR"


class Result(XmlRoot):
    comment: str = XmlAttribute(name="comment")
    eventid: int = XmlAttribute(name="eventid", required=True)
    heatid: int = XmlAttribute(name="heatid")
    lane: int = XmlAttribute(name="lane")
    points: int = XmlAttribute(name="points")
    reactionTime: ReactionTime = XmlAttribute(name="reactiontime")
    relayPositions: List[RelayPosition] = XmlElementWrapper(name="RELAYPOSITIONS")
    resultid: int = XmlAttribute(name="resultid", required=True)
    status: StatusResult = XmlAttribute(name="status")
    splits: List[Split] = XmlElementWrapper(name="SPLITS")
    swimTime: SwimTime = XmlAttribute(name="swimtime")
