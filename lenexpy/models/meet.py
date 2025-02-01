from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.agedate import AgeDate
from lenexpy.models.nation import Nation
from lenexpy.models.pointtable import PointTable
from lenexpy.models.pool import Pool
from lenexpy.models.qualify import Qualify
from lenexpy.models.session import Session
from lenexpy.models.timing import Timing
from .course import Course
from .contact import Contact
from .club import Club
from .fee import Fee


class EntryType(StrEnum):
    OPEN = 'OPEN'
    INVITATION = 'INVITATION'


class Meet(XmlRoot):
    agedate: AgeDate = XmlElement(name="AGEDATE")
    altitude: int = XmlAttribute(name="altitude")
    city: str = XmlAttribute(name="city", required=True)
    cityEn: str = XmlAttribute(name="city.en")
    clubs: List[Club] = XmlElement(name="CLUB")
    contact: Contact = XmlElement(name="CONTACT")
    course: Course = XmlAttribute(name="course")
    deadline: LocalDate = XmlAttribute(name="deadline")
    deadline_time: LocalTime = XmlAttribute(name="deadlinetime")
    entry_start_date: LocalDate = XmlAttribute(name="entrystartdate")
    entry_type: EntryType = XmlAttribute(name="entrytype")
    fees: List[Fee] = XmlElement(name="FEE")
    host_club: str = XmlAttribute(name="hostclub")
    host_club_url: str = XmlAttribute(name="hostclub.url")
    max_entries: int = XmlAttribute(name="maxentries")
    name: str = XmlAttribute(name="name", required=True)
    name_en: str = XmlAttribute(name="name.en")
    nation: Nation = XmlAttribute(name="nation", required=True)
    number: str = XmlAttribute(name="number")
    organizer: str = XmlAttribute(name="organizer")
    organizer_url: str = XmlAttribute(name="organizer.url")
    point_table: PointTable = XmlElement(name="POINTTABLE")
    pool: Pool = XmlElement(name="POOL")
    qualify: Qualify = XmlElement(name="QUALIFY")
    result_url: str = XmlAttribute(name="result.url")
    sessions: List[Session] = XmlElementWrapper("SESSIONS", 'SESSION', required=True)
    state: str = XmlAttribute(name="state")
    uid: str = XmlAttribute(name="swrid")
    timing: Timing = XmlAttribute(name="timing")
    type: str = XmlAttribute(name="type")
