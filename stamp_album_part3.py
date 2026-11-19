# === Stage 3: Хранилище в памяти ===
# Project: StampAlbum
"""StampAlbum - in-memory storage module for stamp entities.

This module provides a simple, self-contained in-memory store for
stamp records. Each stamp is identified by a unique id, and the store
supports adding new stamps, retrieving them by id, and listing them all.

Only the Python standard library is used.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Stamp:
    """A single postage stamp.

    Attributes:
        id: Unique identifier of the stamp within the store.
        name: Name or description of the stamp.
        country: Country of origin.
        year: Year of issue.
        value: Denomination or face value of the stamp.
    """

    id: str
    name: str
    country: str
    year: int
    value: float


class StampStore:
    """An in-memory collection of stamps.

    The store keeps stamps in a dictionary keyed by their id, which
    allows constant-time lookup. It is safe for basic sequential use
    and does not share internal state with any other object.
    """

    def __init__(self) -> None:
        self._stamps: Dict[str, Stamp] = {}

    def add(self, stamp: Stamp) -> None:
        """Add a stamp to the store.

        If a stamp with the same id already exists, it is replaced.
        """
        self._stamps[stamp.id] = stamp

    def get(self, stamp_id: str) -> Optional[Stamp]:
        """Return the stamp with the given id, or None if not found."""
        return self._stamps.get(stamp_id)

    def list_all(self) -> List[Stamp]:
        """Return all stamps currently in the store.

        The returned list is a shallow copy of the internal list, so
        mutating the result does not affect the store.
        """
        return list(self._stamps.values())

    def __len__(self) -> int:
        """Return the number of stamps in the store."""
        return len(self._stamps)

    def __contains__(self, stamp_id: object) -> bool:
        """Support the 'in' operator for membership checks by id."""
        return stamp_id in self._stamps
