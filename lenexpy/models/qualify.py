from enum import StrEnum
from xmlbind import XmlRoot, XmlAttribute, XmlElement
from datetime import datetime, time as dtime


class Conversion(StrEnum):
    NONE = "NONE"
    FINA_POINTS = " FINA_POINTS"
    PERCENT_LINEAR = " PERCENT_LINEAR"
    NON_CONFORMING_LAST = " NON_CONFORMING_LAST"


class Qualify(XmlRoot):
    conversion: Conversion = XmlAttribute(name="conversion")
    from_: dtime = XmlAttribute(name="from", required=True)
    percent: int = XmlAttribute(name="percent")
    until: dtime = XmlAttribute(name="until")
