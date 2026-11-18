# === Stage 2: Проверка полей ===
# Project: StampAlbum
"""Validation and input normalization helpers for the StampAlbum 'stamp' entity."""

from typing import Optional, Tuple


def normalize_country(value: str) -> str:
    """Return the country text trimmed and lower-cased."""
    return value.strip().lower()


def normalize_name(value: str) -> str:
    """Return the name text with surrounding whitespace removed."""
    return value.strip()


def normalize_year(value: str) -> int:
    """Parse a year string into an int, raising ValueError on bad input."""
    cleaned = value.strip()
    if not cleaned:
        raise ValueError("Year must not be empty.")
    try:
        year = int(cleaned)
    except ValueError:
        raise ValueError(f"Year '{cleaned}' is not a number.")
    if year < 1:
        raise ValueError("Year must be positive.")
    return year


def normalize_face_value(value: str) -> float:
    """Parse a face value string into a non-negative float, raising ValueError."""
    cleaned = value.strip()
    if not cleaned:
        raise ValueError("Face value must not be empty.")
    try:
        face = float(cleaned)
    except ValueError:
        raise ValueError(f"Face value '{cleaned}' is not a number.")
    if face < 0:
        raise ValueError("Face value must not be negative.")
    return face


def validate_stamp(
    name: str,
    country: str,
    year: str,
    face_value: str,
) -> Tuple[str, str, int, float]:
    """Validate and normalize stamp fields.

    Raises ValueError with a descriptive message on the first invalid field:
    name, country, year, then face_value.

    Returns a tuple (normalized_name, normalized_country, year, face_value).
    """
    name = normalize_name(name)
    if not name:
        raise ValueError("Stamp name must not be empty.")

    country = normalize_country(country)
    if not country:
        raise ValueError("Country must not be empty.")

    year = normalize_year(year)

    face_value = normalize_face_value(face_value)

    return name, country, year, face_value
