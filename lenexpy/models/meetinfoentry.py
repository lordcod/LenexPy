from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.pool import Pool
from lenexpy.models.swimtime import SwimTime
from .course import Course


class MeetInfoEntry(XmlRoot):
    approved: str = XmlAttribute(name="approved")
    city: str = XmlAttribute(name="city", required=True)
    course: Course = XmlAttribute(name="course")
    date: LocalDate = XmlAttribute(name="date", required=True)
    daytime: LocalTime = XmlAttribute(name="daytime")
    name: str = XmlAttribute(name="name")
    nation: str = XmlAttribute(name="nation", required=True)
    pool: Pool = XmlElement(name="POOL")
    qualification_time: SwimTime = XmlAttribute(name="qualificationtime")
    state: str = XmlAttribute(name="state")
