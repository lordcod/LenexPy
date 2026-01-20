import lenexpy
import dianpy
from dianpy.athlete import Athlete

path = r"C:\Users\2008d\OneDrive\Документы\Соревнования\20.04.25 Кубок Главы Власиха\Кубок_ГЛАВЫ_г_о_В_ХА_ФИНАЛ,_20_04_2025.Swimming"
path_lenex = r"C:\Users\2008d\OneDrive\Документы\Соревнования\20.04.25 Кубок Главы Власиха\lenex.lxf"


dian = dianpy.fromfile(path)
lenex = lenexpy.fromfile(path_lenex)

de = dian.events[9]
le = lenex.meet.sessions[0].events[9]
event_id = le.eventid

for club in lenex.meet.clubs:
    for athl in club.athletes or []:
        for entry in athl.entries or []:
            if entry.eventid != event_id:
                continue
            da = Athlete(
                firstname=athl.firstname,
                lastname=athl.lastname,
                birthdate=athl.birthdate.strftime('%d.%m.%Y'),
                club=club.name,
                gender=athl.gender,
                entrytime=""
            )
            if de.athletes is None:
                de.athletes = []
            de.athletes.append(da)

dianpy.tofile(dian, 'test.xml')
