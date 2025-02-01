

text = """
    @XmlAttribute(name = "city")
    private String city;
    @XmlAttribute(name = "country")
    private String country;
    @XmlAttribute(name = "email", required = true)
    private String email;
    @XmlAttribute(name = "fax")
    private String fax;
    @XmlAttribute(name = "internet")
    private String internet;
    @XmlAttribute(name = "name")
    private String name;
    @XmlAttribute(name = "mobile")
    private String mobile;
    @XmlAttribute(name = "phone")
    private String phone;
    @XmlAttribute(name = "state")
    private String state;
    @XmlAttribute(name = "street")
    private String street;
    @XmlAttribute(name = "street2")
    private String street2;
    @XmlAttribute(name = "zip")
    private String zip;
""".replace('    ', '')

final = []
for adapter in text.split(';'):
    if not adapter.strip('\n'):
        continue
    *decors, vars = adapter.strip('\n').split('\n')
    vars = vars.removeprefix('private ').replace('<', '[').replace('>', ']').replace('String', 'str')
    v1, v2 = vars.split(' ')[::-1]
    final.append(
        v1 + ': ' + v2
        + ' = '
        + decors[-1].removeprefix('@').replace('true', 'True')
    )

print(final)
with open('text.py', 'wb+') as file:
    file.write('\n    '.join(final).encode())
