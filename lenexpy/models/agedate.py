from enum import StrEnum
from xmlbind import XmlRoot, XmlAttribute, XmlElement
from datetime import datetime, time as dtime


class TypeAgeDate(StrEnum):
    YEAR = "YEAR"
    DATE = "DATE"
    POR = "POR"
    CAN_FNQ = "CAN.FNQ"
    LUX = "LUX"


class AgeDate(XmlRoot):
    type: TypeAgeDate = XmlAttribute(name="type", required=True)
    value: dtime = XmlAttribute(name="value", required=True)
