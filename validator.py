from xmlbind import XmlRoot, XmlElement, XmlElementWrapper, XmlAttribute


def validate_type(root: XmlRoot):
    cls = type(root)
    data = root.__dict__
    annotations = cls.__annotations__
    for name, value in cls.__dict__.items():
        if name in data and data[name] is None:
            continue
        if isinstance(value, (XmlElement, XmlElementWrapper)):
            if not isinstance(data[name], (XmlRoot, list)):
                print('No validate root', name, data[name])
                continue
            if isinstance(data[name], list):
                for d in data[name]:
                    validate_type(d)
            else:
                validate_type(data[name])
        if isinstance(value, XmlAttribute):
            if not isinstance(data[name], annotations[name]):
                print('No validate attr', name, data[name], annotations[name])
