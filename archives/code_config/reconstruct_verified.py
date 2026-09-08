#!/usr/bin/env python3
"""Reconstruct and verify the frozen Residual181 public code/config archive.

Legacy parts 15, 17, and 18 on the repository history are intentionally not
used. Their verified replacement text is stored in corrections/.
"""
from __future__ import annotations

import base64
import hashlib
from pathlib import Path
import sys
import zipfile

EXPECTED_SHA256 = "093ef05675fecd3a4e41e9dd3765aa3920d8cff834ff12179a1a58bb146a0a2c"
EXPECTED_FILES = 61
ROOT = Path(__file__).resolve().parent


def read(name: str) -> str:
    text = (ROOT / name).read_text(encoding="utf-8")
    return "".join(text.split())


def main() -> int:
    segments: list[str] = []
    for i in range(1, 15):
        segments.append(read(f"RVC_CODE_CONFIG_COMPLETE.zip.b64.part{i:02d}"))

    # Verified replacements for legacy malformed part 15.
    segments.append(
        read("corrections/part15.a")
        + read("corrections/part15.b1")
        + read("corrections/part15.b2")
    )

    segments.append(read("RVC_CODE_CONFIG_COMPLETE.zip.b64.part16"))

    # Verified replacements for legacy malformed parts 17 and 18.
    segments.append(read("corrections/part17.a") + read("corrections/part17.b"))
    segments.append(read("corrections/part18.a") + read("corrections/part18.b"))
    segments.append(read("RVC_CODE_CONFIG_COMPLETE.zip.b64.part19"))

    encoded = "".join(segments)
    try:
        payload = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        print(f"FAIL: Base64 decoding failed: {exc}", file=sys.stderr)
        return 2

    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        print(
            f"FAIL: SHA-256 mismatch: got {digest}, expected {EXPECTED_SHA256}",
            file=sys.stderr,
        )
        return 3

    out = ROOT / "RVC_CODE_CONFIG_COMPLETE.zip"
    out.write_bytes(payload)

    try:
        with zipfile.ZipFile(out) as zf:
            bad = zf.testzip()
            names = [n for n in zf.namelist() if not n.endswith("/")]
    except zipfile.BadZipFile as exc:
        print(f"FAIL: reconstructed payload is not a valid ZIP: {exc}", file=sys.stderr)
        return 4

    if bad is not None:
        print(f"FAIL: ZIP CRC failure in {bad}", file=sys.stderr)
        return 5
    if len(names) != EXPECTED_FILES:
        print(
            f"FAIL: expected {EXPECTED_FILES} files in ZIP, found {len(names)}",
            file=sys.stderr,
        )
        return 6

    print(f"PASS: {out.name}")
    print(f"SHA-256: {digest}")
    print(f"ZIP files: {len(names)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
