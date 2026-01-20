import json
from datetime import datetime

from lenexpy import tofile
from lenexpy.models.agegroup import AgeGroup
from lenexpy.models.constructor import Constructor
from lenexpy.models.course import Course
from lenexpy.models.event import Event
from lenexpy.models.gender import Gender
from lenexpy.models.lenex import Lenex
from lenexpy.models.meet import Meet
from lenexpy.models.pool import Pool, TypePool
from lenexpy.models.session import Session
from lenexpy.models.swimstyle import SwimStyle


def parse_agegroup(ag_json):
    return AgeGroup(
        id=ag_json.get("id"),
        agemin=ag_json["agemin"],
        agemax=ag_json["agemax"],
        gender=Gender(ag_json.get("gender")) if ag_json.get(
            "gender") else None,
        name=ag_json.get("name")
    )


def parse_swimstyle(sw_json):
    return SwimStyle(
        distance=sw_json["distance"],
        relaycount=sw_json["relaycount"],
        stroke=sw_json["stroke"],
        name=sw_json.get("name"),
        code=sw_json.get("code"),
        swimstyleid=sw_json.get("swimstyleid")
    )


def parse_event(order, ev_json):
    ags_json = ev_json.get("agegroups", [])
    if not isinstance(ags_json, list):
        ags_json = []
    return Event(
        eventid=ev_json["eventid"],
        number=ev_json["number"],
        gender=Gender(ev_json.get("gender")) if ev_json.get(
            "gender") else None,
        swimstyle=parse_swimstyle(ev_json["swimstyle"]),
        agegroups=[parse_agegroup(ag) for ag in ags_json],
        order=order,
        preveventid=-1
    )


def parse_session(s_json):
    return Session(
        number=s_json["number"],
        name=s_json.get("name"),
        date=datetime.fromisoformat(s_json["date"]),
        events=[parse_event(order, ev)
                for order, ev in enumerate(s_json.get("events", []), start=1)]
    )


def parse_pool(p_json):
    return Pool(
        name=p_json.get("name"),
        lanemin=p_json.get("lanemin"),
        lanemax=p_json.get("lanemax"),
        type=TypePool(p_json.get("type")),
        temperature=p_json.get("temperature")
    )


def parse_meet(meet_json):
    meet = Meet(
        name=meet_json["name"],
        city=meet_json["city"],
        nation=meet_json["nation"],
        sessions=[]
    )
    if "pool" in meet_json:
        meet.pool = parse_pool(meet_json["pool"])
    if "sessions" in meet_json:
        meet.sessions = [parse_session(s) for s in meet_json["sessions"]]
    return meet


def create_lenex_from_json(json_data):
    constructor_json = json_data["constructor"]
    constructor = Constructor(
        name=constructor_json["name"],
        version=constructor_json["version"]
    )

    meet = parse_meet(json_data["meet"])

    return Lenex(
        constructor=constructor,
        meet=meet,
        version=json_data["version"]
    )


if __name__ == "__main__":
    with open("meet.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    lenex_obj = create_lenex_from_json(data)
    tofile(lenex_obj, "meet.lxf")
