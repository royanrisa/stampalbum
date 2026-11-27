# === Stage 17: Смена статуса ===
# Project: StampAlbum
from enum import Enum


class StampStatus(Enum):
    ACQUIRED = "acquired"
    EXCHANGED_OUT = "exchanged_out"
    EXCHANGED_IN = "exchanged_in"


_TRANSITIONS = {
    StampStatus.ACQUIRED: {
        StampStatus.EXCHANGED_OUT: "sold_from_collection",
        StampStatus.EXCHANGED_IN: "exchanged_into_collection",
    },
    StampStatus.EXCHANGED_IN: {
        StampStatus.EXCHANGED_OUT: "sold_from_collection",
    },
    StampStatus.EXCHANGED_OUT: set(),
}


def change_stamp_status(stamp, new_status, reason):
    current = stamp.status
    if new_status == current:
        raise ValueError(f"Stamp {stamp.name} is already in status {current.value}")
    allowed = _TRANSITIONS.get(current, set())
    if new_status not in allowed:
        raise ValueError(
            f"Invalid transition from {current.value} to {new_status.value}"
        )
    if not reason or not reason.strip():
        raise ValueError("Reason must not be empty")
    stamp.status = new_status
    stamp.last_reason = reason
    stamp.last_changed_on = _now()
    return stamp


def _now():
    from datetime import datetime

    return datetime.now().isoformat(timespec="seconds")


class Stamp:
    def __init__(self, name, country, year, denomination):
        self.name = name
        self.country = country
        self.year = year
        self.denomination = denomination
        self.status = StampStatus.ACQUIRED
        self.last_reason = None
        self.last_changed_on = None
