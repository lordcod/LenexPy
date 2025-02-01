from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.meetinfoentry import MeetInfoEntry
from lenexpy.models.replayposition import RelayPosition
from lenexpy.models.swimtime import SwimTime
from .course import Course


class Status(StrEnum):
    EXH = "EXH"
    RJC = "RJC"
    SICK = "SICK"
    WDR = "WDR"


class Entry(XmlRoot):
    agegroupid: int = XmlAttribute(name="agegroupid")
    entrycourse: Course = XmlAttribute(name="entrycourse")
    entrytime: SwimTime = XmlAttribute(name="entrytime")
    eventid: int = XmlAttribute(name="eventid", required=True)
    heatid: int = XmlAttribute(name="heatid")
    lane: int = XmlAttribute(name="lane")
    meetinfo: MeetInfoEntry = XmlElement(name="MEETINFO")
    relayPositions: List[RelayPosition] = XmlElementWrapper(name="RELAYPOSITIONS")
    status: Status = XmlAttribute(name="status")
