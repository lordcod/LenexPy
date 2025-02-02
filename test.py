import lxml.etree as ET
from lenexpy import fromfile

filename = r"C:\Users\2008d\OneDrive\Документы\Соревнования\31.01.2025 Наро-Фоминск\Заявка\entries.lxf"
lenex = fromfile(filename)

for c in lenex.meet.clubs:
    for a in c.athletes:
        print(a.birthdate, type(a.birthdate))


el = lenex.dump('LENEX')
text = ET.tostring(
    el,
    encoding='utf-8',
    xml_declaration=True,
    method='xml'
)
open('test2.xml', 'wb').write(text)
