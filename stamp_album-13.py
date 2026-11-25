# === Stage 13: Поиск дубликатов ===
# Project: StampAlbum
from typing import List, Dict, Tuple

NORMALIZATION_MAP: Dict[str, str] = {
    "name": "strip_name",
    "country": "strip_country",
    "year": "normalize_year",
    "denomination": "normalize_denomination",
}

def strip_name(value: str) -> str:
    return value.strip().lower()

def strip_country(value: str) -> str:
    return value.strip().lower()

def normalize_year(value) -> str:
    if isinstance(value, (int, float)):
        return str(int(value))
    cleaned = str(value).strip().lower()
    for prefix in ("c.", "ca.", "circa", "approx"):
        if cleaned.startswith(prefix):
            cleaned = cleaned[len(prefix):].strip()
            break
    digits = "".join(ch for ch in cleaned if ch.isdigit())
    return digits if digits else cleaned

def normalize_denomination(value) -> str:
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value).strip().lower()
    for prefix in ("$", "us", "e", "eur", "€", "₽", "р"):
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
            break
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits if digits else text

def normalize_stamp(stamp: Dict[str, str]) -> Tuple[str, str, str, str]:
    fields = [
        NORMALIZATION_MAP["name"](stamp.get("name", "")),
        NORMALIZATION_MAP["country"](stamp.get("country", "")),
        NORMALIZATION_MAP["year"](stamp.get("year", "")),
        NORMALIZATION_MAP["denomination"](stamp.get("denomination", "")),
    ]
    return tuple(fields)

def find_duplicates(stamps: List[Dict[str, str]]) -> List[Dict[str, str]]:
    seen: Dict[Tuple[str, str, str, str], List[Dict[str, str]]] = {}
    for stamp in stamps:
        signature = normalize_stamp(stamp)
        seen.setdefault(signature, []).append(stamp)
    duplicates = [group for group in seen.values() if len(group) > 1]
    return duplicates

def get_duplicate_count(stamps: List[Dict[str, str]]) -> int:
    signature_count: Dict[Tuple[str, str, str, str], int] = {}
    for stamp in stamps:
        signature = normalize_stamp(stamp)
        signature_count[signature] = signature_count.get(signature, 0) + 1
    return sum(count - 1 for count in signature_count.values() if count > 1)
