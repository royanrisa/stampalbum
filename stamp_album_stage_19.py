# === Stage 19: Просмотр истории ===
# Project: StampAlbum
from __future__ import annotations


def format_stamp_record(stamp: dict) -> str:
    country = stamp.get("country", "Unknown")
    year = stamp.get("year", "n/a")
    denomination = stamp.get("denomination", "n/a")
    return f"[{year}] {country} {denomination}"


def stamp_history_view(stamp: dict, lines: int = 6) -> str:
    country = stamp.get("country", "Unknown")
    year = stamp.get("year", "n/a")
    title = stamp.get("title", "Untitled")
    denomination = stamp.get("denomination", "n/a")
    header = f"=== {title} ({year}, {country}) ==="
    body = f"Title:    {title}\nCountry:  {country}\nYear:     {year}\nDenomination: {denomination}"
    return header + "\n" + body
