from enum import StrEnum
from xmlbind import XmlRoot, XmlAttribute, XmlElement
from .contact import Contact
from .gender import Gender


class TypePool(StrEnum):
    INDOOR = "INDOOR"
    OUTDOOR = " OUTDOOR"
    LAKE = " LAKE"
    OCEAN = " OCEAN"


class Pool(XmlRoot):
    name: str = XmlAttribute(name="name")
    lanemax: int = XmlAttribute(name="lanemax")
    lanemin: int = XmlAttribute(name="lanemin")
    temperature: int = XmlAttribute(name="temperature")
    type: TypePool = XmlAttribute(name="type")
