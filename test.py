from datetime import date
from lenexpy import fromfile, tofile
from lenexpy.models.athelete import Athlete
from lenexpy.models.club import Club
from lenexpy.models.entry import Entry
from lenexpy.models.swimtime import SwimTime
from validator import validate_type

filename = "testlb.lef"
lenex_lb = fromfile(filename)
validate_type(lenex_lb)


filename = "test.lef"
lenex2 = fromfile(filename)
validate_type(lenex2)

# import athl from meet to meet
for cl in lenex_lb.meet.clubs:
    for athl in cl.athletes:
        athl.entries = []
        athl.results = []

lenex2.meet.clubs = lenex_lb.meet.clubs


# add club and athl
vostok = Club(
    'СШОР ВОСТОК',
    'ВОСТОК'
)
athl = Athlete(
    1900,
    birthdate=date(2008, 12, 24),
    gender='M',
    firstname='Аникин',
    lastname='Даниил'
)
entry = Entry(
    SwimTime.NT
)
lenex2.meet.clubs.append(vostok)
vostok.athletes.append(athl)

tofile(lenex2, 'test2.lef')
