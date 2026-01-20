import json
import tempfile
import unittest

from lenexpy import tofile
from lenexpy.decoder.lef_decoder import decode_lef_bytes
from lenexpy.decoder.lef_encoder import encode_lef_bytes
from lenexpy.decoder.lxf_decoder import decode_lxf_bytes
from lenexpy.decoder.lxf_encoder import encode_lxf_bytes
from lenexpy.models.constructor import Constructor
from lenexpy.models.lenex import Lenex
from lenexpy.models.meet import Meet
from scripts.parser import create_lenex_from_json, create_lenex_from_json_file


class TestParser(unittest.TestCase):
    def _make_lenex(self) -> Lenex:
        constructor = Constructor(name="Bot", version="1.0.0")
        meet = Meet(name="Test Meet", city="City", nation="RUS", sessions=[])
        return Lenex(constructor=constructor, meet=meet, version="3.0")

    def test_parse_minimal_lenex(self):
        data = {
            "version": "3.0",
            "constructor": {"name": "Bot", "version": "1.0.0"},
            "meet": {"name": "Test Meet", "city": "City", "nation": "RUS"},
        }

        lenex = create_lenex_from_json(data)

        self.assertEqual(lenex.version, "3.0")
        self.assertEqual(lenex.constructor.name, "Bot")
        self.assertEqual(lenex.meet.name, "Test Meet")
        self.assertEqual(lenex.meet.city, "City")
        self.assertEqual(lenex.meet.nation, "RUS")

    def test_parse_event_with_agegroups(self):
        data = {
            "version": "3.0",
            "constructor": {"name": "Bot", "version": "1.0.0"},
            "meet": {
                "name": "Test Meet",
                "city": "City",
                "nation": "RUS",
                "sessions": [
                    {
                        "number": 1,
                        "date": "2025-02-02T00:00:00",
                        "events": [
                            {
                                "eventid": 1,
                                "number": 1,
                                "gender": "M",
                                "swimstyle": {
                                    "distance": 100,
                                    "relaycount": 1,
                                    "stroke": "FREE",
                                    "name": "Free",
                                },
                                "agegroups": [
                                    {
                                        "id": 10,
                                        "agemin": 14,
                                        "agemax": 18,
                                        "gender": "M",
                                        "name": "Boys",
                                    }
                                ],
                            }
                        ],
                    }
                ],
            },
        }

        lenex = create_lenex_from_json(data)
        session = lenex.meet.sessions[0]
        event = session.events[0]

        self.assertEqual(event.eventid, 1)
        self.assertEqual(event.gender, "M")
        self.assertEqual(event.swimstyle.stroke, "FREE")
        self.assertEqual(len(event.agegroups), 1)
        self.assertEqual(event.agegroups[0].agemin, 14)

    def test_encode_decode_lef_bytes(self):
        lenex = self._make_lenex()
        xml_bytes = encode_lef_bytes(lenex)
        decoded = decode_lef_bytes(xml_bytes)
        self.assertEqual(decoded.version, lenex.version)
        self.assertEqual(decoded.meet.name, lenex.meet.name)

    def test_encode_decode_lxf_bytes(self):
        lenex = self._make_lenex()
        lxf_bytes = encode_lxf_bytes(lenex, "meet.lxf")
        decoded = decode_lxf_bytes(lxf_bytes)
        self.assertEqual(decoded.constructor.name, lenex.constructor.name)

    def test_to_file_writes_outputs(self):
        lenex = self._make_lenex()
        with tempfile.TemporaryDirectory() as tmpdir:
            lef_path = f"{tmpdir}/meet.lef"
            lxf_path = f"{tmpdir}/meet.lxf"
            tofile(lenex, lef_path)
            tofile(lenex, lxf_path)
            with open(lef_path, "rb") as f:
                self.assertTrue(f.read())
            with open(lxf_path, "rb") as f:
                self.assertTrue(f.read())

    def test_parse_from_json_file(self):
        data = {
            "version": "3.0",
            "constructor": {"name": "Bot", "version": "1.0.0"},
            "meet": {"name": "File Meet", "city": "City", "nation": "RUS"},
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            json_path = f"{tmpdir}/meet.json"
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f)

            lenex = create_lenex_from_json_file(json_path)
            self.assertEqual(lenex.meet.name, "File Meet")


if __name__ == "__main__":
    unittest.main()
