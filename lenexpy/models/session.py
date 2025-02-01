from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.event import Event
from lenexpy.models.fee import Fee
from lenexpy.models.judge import Judge
from lenexpy.models.pool import Pool

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


class Session(XmlRoot):
    course: Course = XmlAttribute(name="course")
    date: LocalDate = XmlAttribute(name="date", required=True)  # 2025-02-02
    daytime: LocalTime = XmlAttribute(name="daytime")
    events: List[Event] = XmlElement(name="EVENT", required=True)
    fees: List[Fee] = XmlElementWrapper(name="FEES")
    judges: List[Judge] = XmlElementWrapper(name="JUDGES")
    name: str = XmlAttribute(name="name")
    number: int = XmlAttribute(name="number", required=True)
    officialmeeting: LocalTime = XmlAttribute(name="officialmeeting")
    pool: Pool = XmlElement(name="POOL")
    teamleadermeeting: LocalTime = XmlAttribute(name="teamleadermeeting")
    warmupfrom: LocalTime = XmlAttribute(name="warmupfrom")
    warmupuntil: LocalTime = XmlAttribute(name="warmupuntil")
