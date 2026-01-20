import argparse
from pathlib import Path

from lenexpy import fromfile
from lenexpy.decoder.lef_encoder import encode_lef_bytes
from lenexpy.decoder.lxf_encoder import encode_lxf_bytes


def process_file(path: Path) -> None:
    lenex = fromfile(str(path))
    if path.suffix.lower() == ".lxf":
        encode_lxf_bytes(lenex, path.name)
    else:
        encode_lef_bytes(lenex)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Lenex fixtures by decoding and re-encoding.",
    )
    parser.add_argument(
        "fixtures_dir",
        nargs="?",
        default="tests/fixtures",
        help="Directory with .lef/.xml/.lxf files.",
    )
    args = parser.parse_args()

    fixtures_dir = Path(args.fixtures_dir)
    if not fixtures_dir.exists():
        raise SystemExit(f"Directory not found: {fixtures_dir}")

    files = [
        p for p in fixtures_dir.iterdir()
        if p.is_file() and p.suffix.lower() in {".lef", ".xml", ".lxf"}
    ]
    for path in files:
        process_file(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
