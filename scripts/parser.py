import json
from datetime import datetime
from typing import Any, Mapping

from lenexpy import tofile
from lenexpy.models.agegroup import AgeGroup
from lenexpy.models.constructor import Constructor
from lenexpy.models.course import Course
from lenexpy.models.event import Event
from lenexpy.models.gender import Gender
from lenexpy.models.lenex import Lenex
from lenexpy.models.meet import Meet
from lenexpy.models.contact import Contact
from lenexpy.models.pool import Pool, TypePool
from lenexpy.models.session import Session
from lenexpy.models.stroke import Stroke
from lenexpy.models.swimstyle import SwimStyle


def _require(data: Mapping[str, Any], key: str):
    if key not in data:
        raise KeyError(f"Missing required key: {key}")
    return data[key]


def _require_any(data: Mapping[str, Any], *keys: str):
    for key in keys:
        if key in data:
            return data[key]
    raise KeyError(f"Missing required key, expected one of: {', '.join(keys)}")


def _get(data: Mapping[str, Any], *keys: str, default: Any = None):
    for key in keys:
        if key in data:
            return data[key]
    return default


def _enum(enum_cls, value):
    if value is None or isinstance(value, enum_cls):
        return value
    return enum_cls(value)


def parse_contact(contact_json: Mapping[str, Any]) -> Contact:
    _require(contact_json, "email")
    return Contact(**contact_json)


def parse_agegroup(ag_json: Mapping[str, Any]) -> AgeGroup:
    return AgeGroup(
        id=_require_any(ag_json, "id", "agegroupid"),
        agemin=_require(ag_json, "agemin"),
        agemax=_require(ag_json, "agemax"),
        gender=_enum(Gender, ag_json.get("gender")),
        name=ag_json.get("name"),
    )


def parse_swimstyle(sw_json: Mapping[str, Any]) -> SwimStyle:
    return SwimStyle(
        distance=_require(sw_json, "distance"),
        relaycount=_require(sw_json, "relaycount"),
        stroke=_enum(Stroke, _require(sw_json, "stroke")),
        name=sw_json.get("name"),
        code=sw_json.get("code"),
        swimstyleid=sw_json.get("swimstyleid"),
    )


def parse_event(order: int, ev_json: Mapping[str, Any]) -> Event:
    ags_json = ev_json.get("agegroups", [])
    if not isinstance(ags_json, list):
        ags_json = []
    return Event(
        eventid=_require(ev_json, "eventid"),
        number=_require(ev_json, "number"),
        gender=_enum(Gender, ev_json.get("gender")),
        swimstyle=parse_swimstyle(_require(ev_json, "swimstyle")),
        agegroups=[parse_agegroup(ag) for ag in ags_json],
        order=order,
        preveventid=ev_json.get("preveventid", -1),
    )


def parse_session(s_json: Mapping[str, Any]) -> Session:
    return Session(
        number=_require(s_json, "number"),
        name=s_json.get("name"),
        date=datetime.fromisoformat(_require(s_json, "date")),
        events=[parse_event(order, ev)
                for order, ev in enumerate(s_json.get("events", []), start=1)]
    )


def parse_pool(p_json: Mapping[str, Any]) -> Pool:
    pool_type = _enum(TypePool, p_json.get("type"))
    return Pool(
        name=p_json.get("name"),
        lanemin=p_json.get("lanemin"),
        lanemax=p_json.get("lanemax"),
        type=pool_type,
        temperature=p_json.get("temperature"),
    )


def parse_meet(meet_json: Mapping[str, Any]) -> Meet:
    sessions_json = _require(meet_json, "sessions")
    if not isinstance(sessions_json, list) or len(sessions_json) == 0:
        raise ValueError("Meet.sessions must contain at least one session")

    meet = Meet(
        name=_require(meet_json, "name"),
        city=_require(meet_json, "city"),
        nation=_require(meet_json, "nation"),
        sessions=[parse_session(s) for s in sessions_json],
    )
    if "pool" in meet_json:
        meet.pool = parse_pool(meet_json["pool"])
    return meet


def create_lenex_from_json(json_data: Mapping[str, Any]) -> Lenex:
    constructor_json = _require(json_data, "constructor")
    contact_json = _require(constructor_json, "contact")
    constructor = Constructor(
        name=_require(constructor_json, "name"),
        version=_require(constructor_json, "version"),
        contact=parse_contact(contact_json),
    )

    meet = parse_meet(_require(json_data, "meet"))

    return Lenex(
        constructor=constructor,
        meet=meet,
        version=_require(json_data, "version"),
    )


def create_lenex_from_json_file(filename: str) -> Lenex:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return create_lenex_from_json(data)


def write_lenex_from_json_file(json_filename: str, lenex_filename: str) -> None:
    lenex_obj = create_lenex_from_json_file(json_filename)
    tofile(lenex_obj, lenex_filename)


if __name__ == "__main__":
    write_lenex_from_json_file("meet.json", "meet.lxf")
