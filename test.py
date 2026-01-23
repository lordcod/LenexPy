from pathlib import Path
from lenexpy import fromfile, tofile
from lenexpy.models.heat import Heat
from lenexpy.models.meet import Meet


filename = r"C:\Users\2008d\working-space\LenexPy\meet.xml"
path = Path(filename)
with open(path, "rb") as file:
    meet = Meet.from_xml(file.read())

filename = r"C:\Users\2008d\working-space\LenexPy\heat.xml"
path = Path(filename)
with open(path, "rb") as file:
    heat = Heat.from_xml(file.read())
