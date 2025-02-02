from typing import List
from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper

from .nation import Nation
from .official import Official
from .relaymeet import RelayMeet
from .athelete import Athlete
from .contact import Contact


class TypeClub:
    CLUB = "CLUB",
    NATIONALTEAM = "NATIONALTEAM",
    REGIONALTEAM = "REGIONALTEAM",
    UNATTACHED = "UNATTACHED"


class Club(XmlRoot):
    contact: Contact = XmlElement(name="CONTACT")
    code: str = XmlAttribute(name="code")
    athletes: List[Athlete] = XmlElementWrapper("ATHLETES", "ATHLETE")
    name: str = XmlAttribute(name="name", required=True)
    name_en: str = XmlAttribute(name="name.en")
    nation: Nation = XmlAttribute(name="nation")
    number: int = XmlAttribute(name="number")
    officials: List[Official] = XmlElementWrapper("OFFICIALS", "OFFICIAL")
    region: str = XmlAttribute(name="region")
    relays: List[RelayMeet] = XmlElementWrapper("RELAYS", "RELAY")
    shortname: str = XmlAttribute(name="shortname")
    shortname_en: str = XmlAttribute(name="shortname.en")
    swrid: str = XmlAttribute(name="swrid")
    type: TypeClub = XmlAttribute(name="type")
