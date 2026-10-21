#!/usr/bin/env python3
"""Rebuild annual Brazilian medical-course/institution counts from a normalized e-MEC export.

This script deliberately does not scrape the e-MEC interface or infer dates from current
status. Prepare the input from dated, documented e-MEC records; see docs/RECONSTRUCAO_SERIE_BRASIL.md.
Only rows with a documented effective_start_date enter annual counts. The output is an
inventory-derived series, not automatically a complete national census.
"""
import argparse
import csv
from datetime import date
from pathlib import Path

FIELDS = [
    "course_code", "institution_code", "institution_name", "course_name",
    "effective_start_date", "closure_effective_date", "record_status",
    "source_url", "snapshot_date", "evidence_note",
]

def parse_date(value, field, rownum):
    value = (value or "").strip()
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"linha {rownum}: {field} deve usar AAAA-MM-DD: {value!r}") from exc

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", help="CSV normalizado segundo o modelo em data/")
    parser.add_argument("--output", default="data/br-medical-schools-annual-rebuilt.csv")
    parser.add_argument("--start-year", type=int, default=1808)
    parser.add_argument("--end-year", type=int, default=2025)
    args = parser.parse_args()
    if args.start_year > args.end_year:
        parser.error("--start-year deve ser <= --end-year")

    records = []
    missing_start = 0
    seen_course = set()
    with open(args.input_csv, encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        absent = [field for field in FIELDS if field not in (reader.fieldnames or [])]
        if absent:
            parser.error("colunas obrigatórias ausentes: " + ", ".join(absent))
        for rownum, row in enumerate(reader, start=2):
            code = (row.get("course_code") or "").strip()
            institution = (row.get("institution_code") or "").strip()
            if not code or not institution:
                raise ValueError(f"linha {rownum}: course_code e institution_code são obrigatórios")
            if code in seen_course:
                raise ValueError(f"linha {rownum}: course_code duplicado: {code}")
            seen_course.add(code)
            start = parse_date(row.get("effective_start_date"), "effective_start_date", rownum)
            end = parse_date(row.get("closure_effective_date"), "closure_effective_date", rownum)
            if start and end and end < start:
                raise ValueError(f"linha {rownum}: encerramento anterior ao início")
            if not start:
                missing_start += 1
            records.append((row, start, end))

    output = []
    for year in range(args.start_year, args.end_year + 1):
        cutoff = date(year, 12, 31)
        active = []
        for row, start, end in records:
            # Missing start dates are excluded, never backfilled from the current status.
            if start is None or start > cutoff or (end is not None and end <= cutoff):
                continue
            active.append(row)
        output.append({
            "year": year,
            "active_courses_with_documented_dates": len({r["course_code"].strip() for r in active}),
            "represented_institutions_with_documented_dates": len({r["institution_code"].strip() for r in active}),
            "records_in_input": len(records),
            "records_without_start_date_excluded": missing_start,
            "source_snapshot_coverage": "inventory-derived; completeness not established",
        })
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Registros lidos: {len(records)}; sem data inicial: {missing_start}; anos gerados: {len(output)}")
    print(f"Saída: {destination}")
    print("ATENÇÃO: a série não deve ser publicada como censo nacional até validar cobertura, duplicatas históricas e atos de encerramento.")

if __name__ == "__main__":
    main()
