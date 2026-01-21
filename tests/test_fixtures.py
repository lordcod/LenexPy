from collections import Counter
from pathlib import Path
from zipfile import ZipFile

import lxml.etree as ET

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
        lef_members = [
            m for m in zf.filelist if m.filename.lower().endswith(".lef")]
        member = lef_members[0] if lef_members else zf.filelist[0]
        return zf.read(member)


def _parse_xml(xml_bytes: bytes) -> ET._Element:
    """Parse XML with whitespace stripped to simplify comparisons."""
    parser = ET.XMLParser(remove_blank_text=True)
    return ET.fromstring(xml_bytes, parser=parser)


KEY_ATTRS = (
    "eventid", "number", "id", "agegroupid", "heatid", "lane", "clubid", "athleteid",
    "code", "name"
)


def _child_sig(el) -> str:
    # Короткая подпись: TAG + один “ключевой” атрибут, если есть
    parts = [el.tag]
    for k in KEY_ATTRS:
        v = el.get(k)
        if v is not None:
            parts.append(f"{k}={v}")
            break
    return "<" + " ".join(parts) + ">"


def _children_summary(children) -> str:
    tags = Counter([c.tag for c in children])
    return ", ".join([f"{t}:{n}" for t, n in sorted(tags.items())])


def _compare_elements(original: ET._Element, regenerated: ET._Element, path: str, errors, max_errors: int = 50) -> int:
    """Recursively compare XML elements collecting human-friendly diffs."""
    total = 0

    def record(msg: str):
        nonlocal total
        total += 1
        if len(errors) < max_errors:
            errors.append(msg)

    if original.tag != regenerated.tag:
        record(
            f"{path}: tag differs (orig='{original.tag}', regen='{regenerated.tag}')")
        return total

    # Attributes
    for key, value in original.attrib.items():
        if key not in regenerated.attrib:
            record(f"{path}: missing attribute '{key}' (orig='{value}')")
        # ?
        # elif regenerated.attrib[key] != value:
        #     record(
        #         f"{path}: attribute '{key}' differs (orig='{value}', regen='{regenerated.attrib[key]}')"
        #     )
    for key in regenerated.attrib:
        if key not in original.attrib:
            record(
                f"{path}: unexpected attribute '{key}' present in regenerated xml")

    # Text
    orig_text = (original.text or "").strip()
    regen_text = (regenerated.text or "").strip()
    if orig_text or regen_text:
        if orig_text != regen_text:
            record(
                f"{path}: text differs (orig='{orig_text}', regen='{regen_text}')")

    # Children
    orig_children = list(original)
    regen_children = list(regenerated)
    if len(orig_children) != len(regen_children):
        record(
            f"{path}: children count differs (orig={len(orig_children)}, regen={len(regen_children)})")

    if len(orig_children) != len(regen_children):
        record(
            f"{path}: children count differs "
            f"(orig={len(orig_children)}, regen={len(regen_children)}); "
            f"orig tags: [{_children_summary(orig_children)}]; "
            f"regen tags: [{_children_summary(regen_children)}]"
        )

        # Детализация “хвоста”
        min_len = min(len(orig_children), len(regen_children))

        if len(orig_children) > min_len:
            missing = orig_children[min_len:]
            record(
                f"{path}: regenerated missing {len(missing)} trailing children: "
                + ", ".join(f"{min_len+i+1}:{_child_sig(c)}" for i,
                            c in enumerate(missing))
            )

        if len(regen_children) > min_len:
            extra = regen_children[min_len:]
            record(
                f"{path}: regenerated has {len(extra)} extra trailing children: "
                + ", ".join(f"{min_len+i+1}:{_child_sig(c)}" for i,
                            c in enumerate(extra))
            )

    # Сравнение общего префикса (как и раньше)
    for idx, (orig_child, regen_child) in enumerate(zip(orig_children, regen_children), start=1):
        child_path = f"{path}/{orig_child.tag}[{idx}]"
        total += _compare_elements(orig_child, regen_child,
                                   child_path, errors, max_errors=max_errors)

    return total


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

    orig_root = _parse_xml(original_xml_bytes)
    regen_root = _parse_xml(regenerated_xml_bytes)

    diffs = []
    total = _compare_elements(orig_root, regen_root, orig_root.tag, diffs)
    if total > len(diffs):
        diffs.append(f"...and {total - len(diffs)} more differences")
    if diffs:
        pytest.fail("Roundtrip XML mismatches:\n" + "\n".join(diffs))
