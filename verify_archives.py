
#!/usr/bin/env python3

import argparse
import hashlib
import json
import sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify mesh archives against mesh_catalog.json"
    )
    parser.add_argument(
        "archive_dir", type=Path,
        help="Directory containing the .tgz archives"
    )
    parser.add_argument(
        "--catalog", type=Path,
        default=Path(__file__).resolve().parent / "mesh_catalog.json",
        help="Path to mesh_catalog.json"
    )
    args = parser.parse_args()

    with args.catalog.open(encoding="utf-8") as f:
        catalog = json.load(f)

    archives = catalog["archives"]
    failures = 0

    for entry in archives:
        path = args.archive_dir / entry["filename"]
        expected_size = entry["size_bytes"]
        expected_hash = entry["sha256"].lower()

        label = f"{entry['mesh']} ({entry['variant']})"

        if not path.is_file():
            print(f"FAIL  {label}: missing {path}")
            failures += 1
            continue

        actual_size = path.stat().st_size
        if actual_size != expected_size:
            print(
                f"FAIL  {label}: size mismatch "
                f"({actual_size} != {expected_size})"
            )
            failures += 1
            continue

        actual_hash = sha256_file(path)
        if actual_hash != expected_hash:
            print(f"FAIL  {label}: SHA-256 mismatch")
            print(f"      expected: {expected_hash}")
            print(f"      actual:   {actual_hash}")
            failures += 1
            continue

        print(f"PASS  {label}: {path.name}")

    print(
        f"\nVerified: {len(archives) - failures}/{len(archives)}"
    )

    if failures:
        print("VERIFICATION FAILED")
        return 1

    print("ALL ARCHIVES VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
