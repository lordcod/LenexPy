from datetime import datetime, date
from xmlbind.compiler import XmlCompiler
from xmlbind.settings import add_compiler


class DateCompiler(XmlCompiler[date]):
    def __init__(self):
        super().__init__(date)

    def unmarshal(self, v):
        print('date compil')
        if not v:
            return None
        return date.fromisoformat(v)

    def marshal(self, v):
        if not v:
            return None
        return date.isoformat(v)


class DtCompiler(XmlCompiler[datetime]):
    def __init__(self):
        super().__init__(datetime)

    def unmarshal(self, v):
        print('dt compil')
        if not v:
            return None
        return datetime.strptime(v, "%Y-%m-%d")

    def marshal(self, v):
        if not v:
            return None
        return datetime.strftime(v, "%Y-%m-%d")


class IntCompiler(XmlCompiler[int]):
    def __init__(self):
        super().__init__(int)

    def unmarshal(self, v):
        if not v:
            return None
        return int(v)

    def marshal(self, v):
        if not v:
            return None
        return str(v)


add_compiler(DateCompiler())
add_compiler(DtCompiler())
add_compiler(IntCompiler())
