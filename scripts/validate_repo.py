#!/usr/bin/env python3
"""Validate CSV benchmarks, JSON-LD templates, SVG assets, CITATION.cff, and local Markdown links."""

from __future__ import annotations

import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def strip_fenced_code(md: str) -> str:
    return re.sub(r"```[\s\S]*?```", "", md)


def validate_csvs(errors: list[str]) -> int:
    csv_files = sorted((ROOT / "benchmarks").glob("*.csv"))
    if not csv_files:
        errors.append("No CSV files found under benchmarks/")
        return 0
    for path in csv_files:
        with path.open("r", encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))
        if len(rows) < 2:
            errors.append(f"{path.relative_to(ROOT)}: expected header + at least 1 data row")
            continue
        width = len(rows[0])
        for idx, row in enumerate(rows, start=1):
            if len(row) != width:
                errors.append(
                    f"{path.relative_to(ROOT)}:{idx}: expected {width} columns, got {len(row)}"
                )
            if any(cell.strip() == "" for cell in row):
                errors.append(f"{path.relative_to(ROOT)}:{idx}: contains empty CSV cell")
    return len(csv_files)


def validate_json_templates(errors: list[str]) -> int:
    json_files = sorted((ROOT / "templates").glob("*.json"))
    if not json_files:
        errors.append("No JSON files found under templates/")
        return 0
    for path in json_files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")
            continue
        if "@context" not in data or "@graph" not in data:
            errors.append(f"{path.relative_to(ROOT)}: expected Schema.org @context and @graph")
    return len(json_files)


def validate_svgs(errors: list[str]) -> int:
    svg_files = sorted((ROOT / "assets").glob("*.svg"))
    if not svg_files:
        errors.append("No SVG files found under assets/")
        return 0
    for path in svg_files:
        try:
            ET.fromstring(path.read_text(encoding="utf-8"))
        except ET.ParseError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid SVG XML ({exc})")
    return len(svg_files)


def validate_citation(errors: list[str]) -> None:
    cff = ROOT / "CITATION.cff"
    if not cff.is_file():
        errors.append("Missing CITATION.cff")
        return
    text = cff.read_text(encoding="utf-8")
    for key in ("cff-version:", "title:", "repository-code:", "license:"):
        if key not in text:
            errors.append(f"CITATION.cff missing required field '{key}'")


def validate_markdown_links(errors: list[str]) -> int:
    md_files = sorted(ROOT.rglob("*.md"))
    md_link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    html_attr_re = re.compile(r'\b(?:href|src)="([^"]+)"')

    checked = 0
    for md_path in md_files:
        clean = strip_fenced_code(md_path.read_text(encoding="utf-8"))
        targets = md_link_re.findall(clean) + html_attr_re.findall(clean)
        for raw in targets:
            target = raw.strip().split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            rel_path = target.split("#", 1)[0]
            if not rel_path:
                continue
            resolved = (md_path.parent / rel_path).resolve()
            checked += 1
            if not resolved.exists():
                errors.append(
                    f"{md_path.relative_to(ROOT)}: broken relative reference '{raw}'"
                )
    return checked


def main() -> int:
    errors: list[str] = []
    n_csv = validate_csvs(errors)
    n_json = validate_json_templates(errors)
    n_svg = validate_svgs(errors)
    validate_citation(errors)
    n_links = validate_markdown_links(errors)

    if errors:
        print("Validation failed:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(
        f"OK: validated {n_csv} CSV datasets, {n_json} JSON-LD templates, "
        f"{n_svg} SVG assets, CITATION.cff, and {n_links} local file references."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
