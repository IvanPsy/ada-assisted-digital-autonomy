#!/usr/bin/env python3
"""Build and check the ready-to-wear versions of the student instructions.

Ready-to-wear texts mix two things that change for different reasons:

  - the translation of the core, which depends on the LANGUAGE the parent reads;
  - the local facts (helplines, emergency number, consent age, school names),
    which depend on the COUNTRY the family lives in.

So they live apart, and the files a parent pastes are generated from the pair:

    channels/adult/ready-to-wear/
      _languages/<lang>/template.md   one translation per language (the only file a
                                      translator edits): guide, band file body,
                                      band file names, status wording
      <country>/_country.md           local facts for that country, one JSON block
                                      per language the country is offered in
      <country>/<lang>/               GENERATED: the parent guide (README.md) and
                                      one file per age band

A German-speaking family living in France uses france/de/: German words, French
numbers. Adding that pairing is one JSON block in france/_country.md, no new
translation.

    python3 tools/ready_to_wear.py build        regenerate every generated file
    python3 tools/ready_to_wear.py check        what CI runs (default)
    python3 tools/ready_to_wear.py fingerprint  print the current core fingerprint

`check` fails when:
  - core/core-behavior.md changed after a language template was last reviewed
    against it (its core-fingerprint no longer matches): review the translation,
    then update core-fingerprint in the template and run build;
  - a generated file is missing or differs from what the sources produce
    (someone edited a generated file, or forgot to run build);
  - a paste-ready block is longer than the box it is meant for;
  - a {{PLACEHOLDER}} was left unfilled, or a country asks for a language that
    has no template;
  - the table of countries in the ready-to-wear README is out of date.

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
LANGS = RTW / "_languages"
INDEX = RTW / "README.md"

# From <country>/<lang>/file.md back to the repository root.
TO_ROOT = "../../../../../"

META_RE = re.compile(r"<!--\s*ready-to-wear\s*(.*?)-->", re.S)
COUNTRY_META_RE = re.compile(r"<!--\s*country\s*(.*?)-->", re.S)
JSON_BLOCK = r"<!--\s*{name}\s*-->\s*```json\s*(.*?)```"
LANG_BLOCK_RE = re.compile(r"<!--\s*language:\s*([a-z]{2,3})\s*-->\s*```json\s*(.*?)```", re.S)
GUIDE_MARK = "<!-- guide -->"
BODY_MARK = "<!-- body -->"
LIMIT_RE = re.compile(r"<!--\s*limit:\s*(\d+)\s*-->\s*```text\n(.*?)```", re.S)
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")
INDEX_START = "<!-- countries:start -->"
INDEX_END = "<!-- countries:end -->"


def core_fingerprint() -> str:
    text = CORE.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def utf16_len(s: str) -> int:
    # Web text boxes count UTF-16 units: an emoji counts as 2.
    return len(s.encode("utf-16-le")) // 2


def parse_meta(regex, raw, path):
    m = regex.search(raw)
    if not m:
        raise ValueError(f"{path}: missing header comment")
    meta = {}
    for line in m.group(1).strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def json_block(raw, name, path):
    m = re.search(JSON_BLOCK.format(name=name), raw, re.S)
    if not m:
        raise ValueError(f"{path}: missing <!-- {name} --> json block")
    return json.loads(m.group(1))


def parse_language(path: Path):
    raw = path.read_text(encoding="utf-8")
    meta = parse_meta(META_RE, raw, path)
    bands = json_block(raw, "bands", path)
    status = json_block(raw, "status", path)
    if GUIDE_MARK not in raw or BODY_MARK not in raw:
        raise ValueError(f"{path}: needs both {GUIDE_MARK} and {BODY_MARK}, in that order")
    after_guide = raw.split(GUIDE_MARK, 1)[1]
    guide, body = after_guide.split(BODY_MARK, 1)
    return {
        "meta": meta,
        "bands": bands,
        "status": status,
        "guide": guide.strip("\n") + "\n",
        "body": body.lstrip("\n"),
    }


def parse_country(path: Path):
    raw = path.read_text(encoding="utf-8")
    meta = parse_meta(COUNTRY_META_RE, raw, path)
    offers = {code: json.loads(block) for code, block in LANG_BLOCK_RE.findall(raw)}
    if not offers:
        raise ValueError(f"{path}: no <!-- language: xx --> json block")
    return meta, offers


def fill(text, values):
    for k, v in values.items():
        text = text.replace("{{" + k + "}}", v)
    return text


def check_limits(label, text, meta, errors):
    fill_line = meta.get("fill-line", "")
    reserve = int(meta.get("fill-reserve", "0"))
    found = 0
    for m in LIMIT_RE.finditer(text):
        found += 1
        limit = int(m.group(1))
        block = m.group(2).rstrip("\n")
        n = utf16_len(block)
        has_fill = fill_line in block
        worst = n - (utf16_len(fill_line) if has_fill else 0) + (reserve if has_fill else 0)
        status = "ok" if worst <= limit else "TOO LONG"
        print(f"  {label}: block {found}: {n} chars, {worst} with a {reserve}-char fill line, limit {limit}: {status}")
        if worst > limit:
            errors.append(f"{label}: block {found} is {worst} chars with the fill line, over the {limit} limit")
    if found == 0:
        errors.append(f"{label}: no <!-- limit: N --> text block found")


def generate():
    """Return ({path: text}, index_rows, errors)."""
    errors = []
    fp = core_fingerprint()
    languages = {}
    for tpl in sorted(LANGS.glob("*/template.md")):
        code = tpl.parent.name
        languages[code] = parse_language(tpl)
        got = languages[code]["meta"].get("core-fingerprint")
        if got != fp:
            errors.append(
                f"[{code}] core/core-behavior.md changed since this translation was reviewed "
                f"(template says {got}, core is now {fp}). Review {tpl.relative_to(ROOT)} "
                f"against the core, then set core-fingerprint: {fp} and run build."
            )
    outputs, rows = {}, []
    for cfile in sorted(RTW.glob("*/_country.md")):
        country = cfile.parent
        cmeta, offers = parse_country(cfile)
        for code, data in offers.items():
            label = f"{country.name}/{code}"
            if code not in languages:
                errors.append(f"[{label}] no translation in _languages/{code}/template.md")
                continue
            lang = languages[code]
            status = data.get("status", "untested")
            if status not in lang["status"]:
                errors.append(f"[{label}] status '{status}' has no wording in _languages/{code}/template.md")
                continue
            common = dict(data.get("common", {}))
            common.update({
                "ROOT": TO_ROOT,
                "TEMPLATE_LINK": f"../../_languages/{code}/template.md",
                "COUNTRY_LINK": "../_country.md",
                "STATUS_NOTE": fill(lang["status"][status], common),
                "CORE_VERSION": lang["meta"]["core-version"],
                "CORE_FINGERPRINT": lang["meta"]["core-fingerprint"],
            })
            band_values = []
            for i, band in enumerate(lang["bands"], 1):
                local = data.get("bands", {}).get(band["band"])
                if local is None:
                    errors.append(f"[{label}] no data for band {band['band']}")
                    local = {}
                values = dict(common)
                values.update(local)
                values["FILE"] = band["file"]
                band_values.append(values)
                common[f"B{i}_FILE"] = band["file"]
                for k, v in local.items():
                    common[f"B{i}_{k}"] = v
            texts = {country / code / "README.md": fill(lang["guide"], common)}
            for band, values in zip(lang["bands"], band_values):
                texts[country / code / band["file"]] = fill(lang["body"], values)
            for path, text in texts.items():
                left = sorted(set(PLACEHOLDER_RE.findall(text)))
                if left:
                    errors.append(f"[{label}] {path.name}: unfilled placeholders {left}")
                if path.name != "README.md":
                    check_limits(f"{label}/{path.name}", text, lang["meta"], errors)
            outputs.update(texts)
            rows.append((cmeta.get("name", country.name), lang["meta"].get("language-name", code),
                         f"[{country.name}/{code}/]({country.name}/{code}/)", status))
    return outputs, rows, errors


def index_table(rows):
    lines = ["| Country you live in | Language you read | Guide for the parent | Status |",
             "|---|---|---|---|"]
    for country, language, link, status in rows:
        lines.append(f"| {country} | {language} | {link} | {status} |")
    return f"{INDEX_START}\n" + "\n".join(lines) + f"\n{INDEX_END}"


def run(mode: str) -> int:
    if mode == "fingerprint":
        print(core_fingerprint())
        return 0
    outputs, rows, errors = generate()
    readme = INDEX.read_text(encoding="utf-8")
    if INDEX_START not in readme or INDEX_END not in readme:
        errors.append(f"{INDEX.relative_to(ROOT)}: missing {INDEX_START} / {INDEX_END} markers")
        new_readme = readme
    else:
        before = readme.split(INDEX_START, 1)[0]
        after = readme.split(INDEX_END, 1)[1]
        new_readme = before + index_table(rows) + after
    expected = set(outputs)
    existing = {p for p in RTW.glob("*/*/*.md") if not p.parent.parent.name.startswith("_")}
    if mode == "build":
        for path, text in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print(f"  wrote {path.relative_to(ROOT)}")
        for stale in sorted(existing - expected):
            stale.unlink()
            print(f"  removed {stale.relative_to(ROOT)} (no longer generated)")
        INDEX.write_text(new_readme, encoding="utf-8")
    else:
        for path, text in outputs.items():
            rel = path.relative_to(ROOT)
            if not path.exists():
                errors.append(f"{rel} is missing: run build")
            elif path.read_text(encoding="utf-8") != text:
                errors.append(f"{rel} differs from its sources: edit the language template or _country.md, not the generated file, then run build")
        for stale in sorted(existing - expected):
            errors.append(f"{stale.relative_to(ROOT)} is not generated by anything: remove it or run build")
        if new_readme != readme:
            errors.append(f"{INDEX.relative_to(ROOT)}: the table of countries is out of date: run build")
    if errors:
        print("\nPROBLEMS:")
        for e in errors:
            print(" - " + e)
        return 1
    print("\nAll ready-to-wear versions are in step with the core and with their sources.")
    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1] if len(sys.argv) > 1 else "check"))
