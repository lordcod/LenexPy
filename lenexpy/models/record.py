from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.meetinforecord import MeetInfoRecord
from lenexpy.models.relayrecord import RelayRecord
from lenexpy.models.split import Split
from lenexpy.models.swimstyle import SwimStyle
from lenexpy.models.swimtime import SwimTime
from .athelete import Athlete


class Record(XmlRoot):
    athlete: Athlete = XmlElement(name="ATHLETE")
    comment: str = XmlAttribute(name="comment")
    meetInfo: MeetInfoRecord = XmlElement(name="MEETINFO")
    relay: RelayRecord = XmlElement(name="RELAY")
    splits: List[Split] = XmlElementWrapper("SPLITS", "SPLIT")
    swimstyle: SwimStyle = XmlElement(name="SWIMSTYLE", required=True)
    swimtime: SwimTime = XmlAttribute(name="swimtime", required=True)
    status: str = XmlAttribute(name="status")
