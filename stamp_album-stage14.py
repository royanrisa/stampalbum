# === Stage 14: Слияние записей ===
# Project: StampAlbum
from __future__ import annotations


def pick_winner(existing: object, candidate: object, *,
                prefer_existing: bool = True) -> object:
    """Return the chosen value for a single field.

    By default the existing value wins; when ``prefer_existing`` is False the
    candidate value is preferred. This keeps field comparison logic in one
    place so every merge step behaves consistently.
    """
    if existing is None:
        return candidate
    if candidate is None:
        return existing
    if prefer_existing:
        return existing
    return candidate


def merge_stamp(a: dict, b: dict) -> dict:
    """Combine two stamp records, field by field.

    Each ``stamp`` is a plain dict with the keys: title, country, year,
    value. For every field the winner is decided by :func:`pick_winner`,
    using the order in which the stamps were supplied (a then b).
    """
    merged: dict = {
        "title": pick_winner(a.get("title"), b.get("title")),
        "country": pick_winner(a.get("country"), b.get("country")),
        "year": pick_winner(a.get("year"), b.get("year")),
        "value": pick_winner(a.get("value"), b.get("value")),
    }
    return merged


def merge_exchanges(a: dict, b: dict) -> dict:
    """Combine two exchange records.

    Each ``exchange`` is a plain dict with the keys: partner, offered_stamp,
    received_stamp. The merge keeps the first exchange when both records
    share a partner, otherwise it merges the offered and received stamps.
    """
    partner_a = a.get("partner")
    partner_b = b.get("partner")

    if partner_a != partner_b:
        merged: dict = {
            "partner": pick_winner(partner_a, partner_b),
            "offered_stamp": a.get("offered_stamp")
            or b.get("offered_stamp"),
            "received_stamp": a.get("received_stamp")
            or b.get("received_stamp"),
        }
        return merged

    offered_a = a.get("offered_stamp") or {}
    offered_b = b.get("offered_stamp") or {}
    received_a = a.get("received_stamp") or {}
    received_b = b.get("received_stamp") or {}

    merged: dict = {
        "partner": partner_a,
        "offered_stamp": merge_stamp(offered_a, offered_b),
        "received_stamp": merge_stamp(received_a, received_b),
    }
    return merged
