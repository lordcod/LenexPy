from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

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


def _normalized_dump(lenex_obj):
    """Produce a deterministic dump for equality checks."""
    return lenex_obj.model_dump(mode="json", exclude_none=True)


def _extract_xml_bytes(path: Path) -> bytes:
    if path.suffix.lower() != ".lxf":
        return path.read_bytes()

    with ZipFile(path, "r") as zf:
        if not zf.filelist:
            raise ValueError(f"Empty archive: {path}")
        lef_members = [m for m in zf.filelist if m.filename.lower().endswith(".lef")]
        member = lef_members[0] if lef_members else zf.filelist[0]
        return zf.read(member)


def _normalize_xml(xml_bytes: bytes) -> bytes:
    """Normalize XML for bytewise comparisons (drop formatting, sort attrs)."""
    root = ET.fromstring(xml_bytes)

    def normalize(elem: ET.Element):
        elem.attrib = {k: elem.attrib[k] for k in sorted(elem.attrib)}
        elem.text = (elem.text or "").strip()
        elem.tail = (elem.tail or "").strip()
        for child in elem:
            normalize(child)

    normalize(root)
    return ET.tostring(root, encoding="utf-8")


@pytest.mark.skipif(not FIXTURE_PATHS, reason="No fixtures found")
@pytest.mark.parametrize("path", FIXTURE_PATHS)
def test_fixture_roundtrip(path: Path):
    lenex = fromfile(str(path))

    if path.suffix.lower() == ".lxf":
        lxf_bytes = encode_lxf_bytes(lenex, path.name)
        decoded = decode_lxf_bytes(lxf_bytes)
    else:
        xml_bytes = encode_lef_bytes(lenex)
        decoded = decode_lef_bytes(xml_bytes)

    assert decoded.version == lenex.version


@pytest.mark.skipif(not FIXTURE_PATHS, reason="No fixtures found")
@pytest.mark.parametrize("path", FIXTURE_PATHS)
def test_fixture_roundtrip_preserves_data(path: Path):
    original = fromfile(str(path))
    original_dump = _normalized_dump(original)

    # Round-trip through raw XML (.lef/.xml)
    xml_bytes = encode_lef_bytes(original)
    xml_roundtrip = decode_lef_bytes(xml_bytes)
    assert _normalized_dump(xml_roundtrip) == original_dump

    # Round-trip through zipped Lenex (.lxf)
    lxf_bytes = encode_lxf_bytes(original, path.with_suffix(".lxf").name)
    lxf_roundtrip = decode_lxf_bytes(lxf_bytes)
    assert _normalized_dump(lxf_roundtrip) == original_dump


@pytest.mark.skipif(not FIXTURE_PATHS, reason="No fixtures found")
@pytest.mark.parametrize("path", FIXTURE_PATHS)
def test_fixture_xml_roundtrip_matches_original_bytes(path: Path):
    original_xml_bytes = _extract_xml_bytes(path)
    lenex = fromfile(str(path))

    regenerated_xml_bytes = encode_lef_bytes(lenex)

    assert _normalize_xml(regenerated_xml_bytes) == _normalize_xml(original_xml_bytes)
