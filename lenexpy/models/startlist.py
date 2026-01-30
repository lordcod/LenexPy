from __future__ import annotations

from typing import List

from lenexpy.models.event import Event
from pydantic_xml import element, wrapped

from .base import LenexBaseXmlModel


class StartList(LenexBaseXmlModel, tag="STARTLIST"):
    events: List[Event] = wrapped(
        "EVENTS",
        element(tag="EVENT"),
        default_factory=list,
    )
