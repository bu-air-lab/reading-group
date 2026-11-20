"""Check data/sessions.csv for common mistakes. Run: python3 tools/check_sessions.py"""
import csv, re, sys
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "data" / "sessions.csv"
expected = ["date", "time", "location", "leader", "title", "authors", "venue", "link", "notes"]
problems = []

with open(path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    if header != expected:
        problems.append(f"Header should be: {','.join(expected)}")
    seen = set()
    for line_no, row in enumerate(reader, start=2):
        if not any(cell.strip() for cell in row):
            continue
        if len(row) != len(expected):
            problems.append(f"Line {line_no}: has {len(row)} fields, expected {len(expected)}. "
                            "A field with a comma probably needs double quotes.")
            continue
        r = dict(zip(expected, row))
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["date"]):
            problems.append(f"Line {line_no}: date '{r['date']}' should look like 2026-12-04")
        if not r["title"].strip():
            problems.append(f"Line {line_no}: title is empty")
        if r["link"] and not r["link"].startswith("http"):
            problems.append(f"Line {line_no}: link should start with http")
        key = (r["date"], r["title"].strip().lower())
        if key in seen:
            problems.append(f"Line {line_no}: duplicate of an earlier row")
        seen.add(key)

if problems:
    print("Found problems:\n  " + "\n  ".join(problems))
    sys.exit(1)
print(f"OK: {path.name} looks good.")
