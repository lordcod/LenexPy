from typing import Optional

from pydantic_xml import attr, element

from .base import LenexBaseXmlModel
from .contact import Contact
from .gender import Gender
from .nation import Nation


class Coach(LenexBaseXmlModel, tag="COACH"):
    contact: Optional[Contact] = element(tag="CONTACT", default=None)
    firstname: Optional[str] = attr(name="firstname", default=None)
    gender: Optional[Gender] = attr(name="gender", default=None)
    lastname: Optional[str] = attr(name="lastname", default=None)
    license: Optional[str] = attr(name="license", default=None)
    nameprefix: Optional[str] = attr(name="nameprefix", default=None)
    nation: Optional[Nation] = attr(name="nation", default=None)
    passport: Optional[str] = attr(name="passport", default=None)
    role: Optional[str] = attr(name="role", default=None)
    coachid: Optional[int] = attr(name="coachid", default=None)
