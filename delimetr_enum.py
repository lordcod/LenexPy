text = """EXH,
        RJC,
        SICK,
        WDR
""".replace('    ', '').replace('\n', '')

vars = text.split(',')
final = []
for v in vars:
    # final.append(
    #     v.replace('(', '=').removesuffix(')')
    # )

    final.append(
        v + ' = "' + v + '"'
    )

with open('text.py', 'wb+') as file:
    file.write('\n'.join(final).encode())
