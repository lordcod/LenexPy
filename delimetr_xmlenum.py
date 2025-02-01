text = """
        @XmlEnumValue("YEAR")YEAR,
        @XmlEnumValue("DATE")DATE,
        @XmlEnumValue("POR")POR,
        @XmlEnumValue("CAN.FNQ")CAN_FNQ,
        @XmlEnumValue("LUX")LUX
""".replace('@XmlEnumValue', '').replace('\n', '').replace('    ', '')

vars = text.split(',')
final = []
for v in vars:
    val, var = v.removeprefix('(').split(')')
    final.append(var+' = '+val)

with open('text.py', 'wb+') as file:
    file.write('\n'.join(final).encode())
