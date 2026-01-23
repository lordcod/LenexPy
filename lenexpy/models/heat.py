from lenexpy.models.common import BaseStatus
from lenexpy.strenum import StrEnum
from typing import List, Optional

from pydantic_xml import attr, element, wrapped

from .base import LenexBaseXmlModel
from .entry import Entry
from datetime import time as dtime


class Final(StrEnum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'


# TODO: confirm root tag for Heat.
class Heat(LenexBaseXmlModel, tag="HEAT"):
    agegroupid: Optional[int] = attr(name="agegroupid", default=None)
    daytime: Optional[dtime] = attr(name="daytime", default=None)
    finaltype: Optional[Final] = attr(name="final", default=None)
    heatid: int = attr(name="heatid")
    name: Optional[str] = attr(name="name", default=None)
    number: int = attr(name="number")
    order: Optional[int] = attr(name="order", default=None)
    status: Optional[BaseStatus] = attr(name="status", default=None)
    entries: List[Entry] = wrapped(
        "ENTRIES",
        element(tag="ENTRY"),
        default_factory=list,
    )
