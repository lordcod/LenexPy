from typing import Optional

from lenexpy.strenum import StrEnum
from pydantic import model_validator
from pydantic_xml import attr

from .base import LenexBaseXmlModel
from .stroke import Stroke


class Technique(StrEnum):
    DIVE = "DIVE"
    GLIDE = "GLIDE"
    KICK = "KICK"
    PULL = "PULL"
    START = "START"
    TURN = "TURN"


class SwimStyle(LenexBaseXmlModel, tag="SWIMSTYLE"):
    code: Optional[str] = attr(name="code", default=None)
    distance: Optional[int] = attr(name="distance", default=None)
    name: Optional[str] = attr(name="name", default=None)
    relaycount: Optional[int] = attr(name="relaycount", default=None)
    stroke: Stroke = attr(name="stroke")
    swimstyleid: Optional[int] = attr(name="swimstyleid", default=None)
    technique: Optional[Technique] = attr(name="technique", default=None)

    @model_validator(mode="after")
    def _require_distance_and_relaycount(self):
        if self.stroke not in (Stroke.UNKNOWN, Stroke.CUSTOM):
            if self.distance is None or self.relaycount is None:
                raise ValueError(
                    "SWIMSTYLE elements must define distance and relaycount")
        return self
