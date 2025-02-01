from enum import StrEnum
from xmlbind import XmlRoot, XmlAttribute, XmlElement
from .contact import Contact
from .gender import Gender


class Ranking(XmlRoot):
    order: int = XmlAttribute(name="order")
    place: int = XmlAttribute(name="place", required=True)
    result_id: int = XmlAttribute(name="resultid", required=True)
