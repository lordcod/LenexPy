from datetime import datetime
from xmlbind.compiler import XmlCompiler
from xmlbind.settings import add_compiler


class DtCompiler(XmlCompiler[datetime]):
    def __init__(self):
        super().__init__(datetime)

    def unmarshal(self, v):
        if not v:
            return None
        return datetime.strptime(v, "%Y-%m-%d")


class IntCompiler(XmlCompiler[int]):
    def __init__(self):
        super().__init__(int)

    def unmarshal(self, v):
        if not v:
            return None
        return int(v)


add_compiler(DtCompiler())
add_compiler(IntCompiler())
