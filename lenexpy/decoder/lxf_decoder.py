import lxml.etree as ET
from zipfile import ZipFile
from lenexpy.models.lenex import Lenex


def decode_lxf(filename: str) -> Lenex:
    with ZipFile(filename) as zp:
        if len(zp.filelist) != 1:
            raise TypeError("Incorrect lenex file")
        with zp.open(zp.filelist[0]) as file:
            data = file.read()

    element = ET.fromstring(data)
    return Lenex._parse(element)
