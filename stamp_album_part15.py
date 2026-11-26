# === Stage 15: Массовое обновление ===
# Project: StampAlbum
from typing import List, Dict, Callable, Tuple

# A single stamp record stored in the album.
Stamp = Dict[str, object]
Field = str
FieldValues = Dict[Field, List[object]]
Condition = Callable[[Stamp], bool]


def _coerce(value: object) -> object:
    """Return value, converting None to an empty string for display."""
    if value is None:
        return ""
    return value


def preview_changes(stamps: List[Stamp], condition: Condition,
                    updates: Dict[Field, object]) -> List[Stamp]:
    """Show which stamps would change before committing the update.

    Returns a list of the stamps that would be affected, so the caller
    can review them before writing ``updates`` to the album.
    """
    affected: List[Stamp] = []
    for stamp in stamps:
        if not condition(stamp):
            continue
        for field, value in updates.items():
            current = _coerce(stamp.get(field))
            proposed = _coerce(value)
            if current != proposed:
                stamp[field] = value
                affected.append(stamp)
                break
    return affected


def apply_updates(stamps: List[Stamp], updates: Dict[Field, object]) -> int:
    """Write ``updates`` into every stamp that matches the default rule.

    The default condition matches all stamps; pass a custom condition to
    target a specific subset. Returns the number of stamps changed.
    """
    changed = 0
    for stamp in stamps:
        for field, value in updates.items():
            if stamp.get(field) != value:
                stamp[field] = value
                changed += 1
                break
    return changed


def build_condition(predicate: Condition = lambda stamp: True) -> Condition:
    """Wrap a predicate so it can be reused as a selection condition."""
    return predicate


def summarize(stamps: List[Stamp], updates: Dict[Field, object]) -> Tuple[int, int]:
    """Return (total_stamps, matched_stamps) for a planned update."""
    total = len(stamps)
    matched = sum(1 for stamp in stamps if build_condition()(stamp))
    return total, matched
