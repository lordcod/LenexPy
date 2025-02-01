from enum import StrEnum
from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from lenexpy.models.nation import Nation
from lenexpy.models.official import Official
from lenexpy.models.relaymeet import RelayMeet
from .athelete import Athlete
from .contact import Contact


class TypeClub:
    CLUB = "CLUB",
    NATIONALTEAM = "NATIONALTEAM",
    REGIONALTEAM = "REGIONALTEAM",
    UNATTACHED = "UNATTACHED"


class Club(XmlRoot):
    athletes: List[Athlete] = XmlElementWrapper("ATHLETES", "ATHLETE")
    code: str = XmlAttribute(name="code")
    contact: Contact = XmlElement(name="CONTACT")
    name: str = XmlAttribute(name="name", required=True)
    name_en: str = XmlAttribute(name="name.en")
    nation: Nation = XmlAttribute(name="nation")
    number: int = XmlAttribute(name="number")
    officials: List[Official] = XmlElementWrapper("OFFICIALS", "OFFICIAL")
    region: str = XmlAttribute(name="region")
    relays: List[RelayMeet] = XmlElementWrapper("RELAYS", "RELAY")
    shortname: str = XmlAttribute(name="shortname")
    shortnameEn: str = XmlAttribute(name="shortname.en")
    swrid: str = XmlAttribute(name="swrid")
    type: TypeClub = XmlAttribute(name="type")
