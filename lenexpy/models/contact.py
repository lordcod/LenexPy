from xmlbind import XmlRoot, XmlAttribute, XmlElement, XmlElementWrapper


class Contact(XmlRoot):
    city: str = XmlAttribute(name="city")
    country: str = XmlAttribute(name="country")
    email: str = XmlAttribute(name="email", required=True)
    fax: str = XmlAttribute(name="fax")
    internet: str = XmlAttribute(name="internet")
    name: str = XmlAttribute(name="name")
    mobile: str = XmlAttribute(name="mobile")
    phone: str = XmlAttribute(name="phone")
    state: str = XmlAttribute(name="state")
    street: str = XmlAttribute(name="street")
    street2: str = XmlAttribute(name="street2")
    zip: str = XmlAttribute(name="zip")
