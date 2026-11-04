#!/usr/bin/env python3
"""Build and check the ready-to-wear versions of the student instructions.

Each language folder in channels/adult/ready-to-wear/<lang>/ holds ONE translated
template (_template.md) and the files generated from it, one per age band.
The template is the only file a translator edits; the band files are output.

    python3 tools/ready_to_wear.py build        regenerate the band files
    python3 tools/ready_to_wear.py check        what CI runs (default)
    python3 tools/ready_to_wear.py fingerprint  print the current core fingerprint

`check` fails when:
  - core/core-behavior.md changed after a template was last reviewed against it
    (the template's core-fingerprint no longer matches): review the translation,
    then update core-fingerprint in the template and run build;
  - a band file is missing or differs from what the template generates
    (someone edited a generated file, or forgot to run build);
  - a paste-ready block is longer than the box it is meant for;
  - a {{PLACEHOLDER}} was left unfilled.

Standard library only. Released under the MIT License (LICENSE-CODE).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "core" / "core-behavior.md"
RTW = ROOT / "channels" / "adult" / "ready-to-wear"

META_RE = re.compile(r"<!--\s*ready-to-wear\s*(.*?)-->", re.S)
BANDS_RE = re.compile(r"<!--\s*bands\s*-->\s*```json\s*(.*?)```", re.S)
BODY_MARK = "<!-- body -->"
LIMIT_RE = re.compile(r"<!--\s*limit:\s*(\d+)\s*-->\s*```text\n(.*?)```", re.S)
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def core_fingerprint() -> str:
    text = CORE.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def utf16_len(s: str) -> int:
    # Web text boxes count UTF-16 units: an emoji counts as 2.
    return len(s.encode("utf-16-le")) // 2


def parse_template(path: Path):
    raw = path.read_text(encoding="utf-8")
    m = META_RE.search(raw)
    if not m:
        raise ValueError(f"{path}: missing <!-- ready-to-wear ... --> header")
    meta = {}
    for line in m.group(1).strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    b = BANDS_RE.search(raw)
    if not b:
        raise ValueError(f"{path}: missing <!-- bands --> json block")
    bands = json.loads(b.group(1))
    if BODY_MARK not in raw:
        raise ValueError(f"{path}: missing {BODY_MARK}")
    body = raw.split(BODY_MARK, 1)[1].lstrip("\n")
    return meta, bands, body


def render(meta, band, body) -> str:
    values = dict(band)
    values["CORE_VERSION"] = meta["core-version"]
    values["CORE_FINGERPRINT"] = meta["core-fingerprint"]
    out = body
    for k, v in values.items():
        if k == "file":
            continue
        out = out.replace("{{" + k + "}}", v)
    return out


def check_limits(path_label, text, meta, errors):
    fill = meta.get("fill-line", "")
    reserve = int(meta.get("fill-reserve", "0"))
    found = 0
    for m in LIMIT_RE.finditer(text):
        found += 1
        limit = int(m.group(1))
        block = m.group(2).rstrip("\n")
        n = utf16_len(block)
        worst = n - (utf16_len(fill) if fill in block else 0) + (reserve if fill in block else 0)
        status = "ok" if worst <= limit else "TOO LONG"
        print(f"  {path_label}: block {found}: {n} chars, {worst} with a {reserve}-char fill line, limit {limit}: {status}")
        if worst > limit:
            errors.append(f"{path_label}: block {found} is {worst} chars with the fill line, over the {limit} limit")
    if found == 0:
        errors.append(f"{path_label}: no <!-- limit: N --> text block found")


def run(mode: str) -> int:
    fp = core_fingerprint()
    if mode == "fingerprint":
        print(fp)
        return 0
    errors = []
    templates = sorted(RTW.glob("*/_template.md"))
    if not templates:
        print("No ready-to-wear templates found.")
        return 0
    for tpl in templates:
        lang = tpl.parent.name
        print(f"[{lang}] {tpl.relative_to(ROOT)}")
        meta, bands, body = parse_template(tpl)
        if meta.get("core-fingerprint") != fp:
            errors.append(
                f"[{lang}] core/core-behavior.md changed since this translation was reviewed "
                f"(template says {meta.get('core-fingerprint')}, core is now {fp}). "
                f"Review {tpl.relative_to(ROOT)} against the core, then set core-fingerprint: {fp} and run build."
            )
        for band in bands:
            target = tpl.parent / band["file"]
            text = render(meta, band, body)
            left = sorted(set(PLACEHOLDER_RE.findall(text)))
            if left:
                errors.append(f"[{lang}] {band['file']}: unfilled placeholders {left}")
            if mode == "build":
                target.write_text(text, encoding="utf-8")
                print(f"  wrote {target.relative_to(ROOT)}")
            else:
                if not target.exists():
                    errors.append(f"[{lang}] {band['file']} is missing: run build")
                elif target.read_text(encoding="utf-8") != text:
                    errors.append(f"[{lang}] {band['file']} differs from the template: edit _template.md, not the generated file, then run build")
            check_limits(f"{lang}/{band['file']}", text, meta, errors)
    if errors:
        print("\nPROBLEMS:")
        for e in errors:
            print(" - " + e)
        return 1
    print("\nAll ready-to-wear versions are in step with the core.")
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1] if len(sys.argv) > 1 else "check"))
