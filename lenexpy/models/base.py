from pydantic import ConfigDict
from pydantic_xml import BaseXmlModel


class LenexBaseXmlModel(BaseXmlModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
