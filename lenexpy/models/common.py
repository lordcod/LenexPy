from lenexpy.strenum import StrEnum


class StartMethod(StrEnum):
    ONE_START = "1"
    TWO_STARTS = "2"


class TouchpadMode(StrEnum):
    ONESIDE = "ONESIDE"
    BOTHSIDE = "BOTHSIDE"


class BaseStatus(StrEnum):
    ENTRIES = "ENTRIES"
    SEEDED = "SEEDED"
    RUNNING = "RUNNING"
    UNOFFICIAL = 'UNOFFICIAL'
    INOFFICIAL = 'INOFFICIAL'
    OFFICIAL = "OFFICIAL"
