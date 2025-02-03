from lenexpy import fromfile, tofile
from validator import validate_type

filename = "test.lxf"
lenex = fromfile(filename)
validate_type(lenex)

lenex.constructor.name = 'Name'

tofile(lenex, 'test2.lef')
