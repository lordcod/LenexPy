from pydantic_xml import attr

from .base import LenexBaseXmlModel

from .swimtime import SwimTime


# TODO: confirm root tag for Split.
class Split(LenexBaseXmlModel, tag="SPLIT"):
    distance: int = attr(name="distance")
    swimTime: SwimTime = attr(name="swimtime")
