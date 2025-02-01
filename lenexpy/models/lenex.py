from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.meet import Meet
from lenexpy.models.recordlist import RecordList
from lenexpy.models.timestandardlist import TimeStandardList
from lenexpy.models.timestandardref import TimeStandardRef
from .constructor import Constructor


class Lenex(XmlRoot):
    constructor: Constructor = XmlElement(name="CONSTRUCTOR", required=True)
    meets: Meet = XmlElementWrapper("MEETS", 'MEET')
    recordLists: List[RecordList] = XmlElementWrapper("RECORDLISTS", "RECORDLIST")
    timeStandardLists: List[TimeStandardList] = XmlElementWrapper("TIMESTANDARDLISTS", "TIMESTANDARDLIST")
    version: str = XmlAttribute(name="version", required=True)
