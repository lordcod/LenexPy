from enum import StrEnum
from xmlbind import XmlRoot, XmlAttribute, XmlElement


class TypeAgeDate(StrEnum):
    YEAR = "YEAR"
    DATE = "DATE"
    POR = "POR"
    CAN_FNQ = "CAN.FNQ"
    LUX = "LUX"


class AgeDate(XmlRoot):
    type: TypeAgeDate = XmlAttribute(name="type", required=True)
    value: LocalDate = XmlAttribute(name="value", required=True)
