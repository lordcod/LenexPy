from pathlib import Path

import pytest

from pydantic import ValidationError

from lenexpy import fromfile
from lenexpy.decoder.lef_decoder import decode_lef_bytes
from lenexpy.decoder.lef_encoder import encode_lef_bytes
from lenexpy.decoder.lxf_decoder import decode_lxf_bytes
from lenexpy.decoder.lxf_encoder import encode_lxf_bytes


FIXTURES_DIR = Path("tests/fixtures")

FIXTURE_PATHS = [
    p for p in FIXTURES_DIR.rglob("*")
    if p.is_file() and p.suffix.lower() in {".lef", ".xml", ".lxf"}
] if FIXTURES_DIR.exists() else []


@pytest.mark.skipif(not FIXTURE_PATHS, reason="No fixtures found")
@pytest.mark.parametrize("path", FIXTURE_PATHS)
def test_fixture_roundtrip(path: Path):
    try:
        lenex = fromfile(str(path))
    except ValidationError as exc:
        pytest.xfail(f"Fixture violates Lenex spec: {exc}")

    if path.suffix.lower() == ".lxf":
        lxf_bytes = encode_lxf_bytes(lenex, path.name)
        decoded = decode_lxf_bytes(lxf_bytes)
    else:
        xml_bytes = encode_lef_bytes(lenex)
        decoded = decode_lef_bytes(xml_bytes)

    assert decoded.version == lenex.version
