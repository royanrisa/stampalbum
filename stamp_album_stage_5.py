# === Stage 5: Удаление и восстановление ===
# Project: StampAlbum
"""StampAlbum: soft-delete support for Stamp entities (Stage 5)."""

from datetime import datetime


class Stamp:
    """A postage stamp with basic metadata and soft-delete state."""

    def __init__(self, name, country, year, value):
        self.id = None
        self.name = name
        self.country = country
        self.year = year
        self.value = value
        self.deleted = False
        self.deleted_at = None

    def __repr__(self):
        return (
            f"Stamp(id={self.id}, name={self.name!r}, country={self.country!r}, "
            f"year={self.year}, value={self.value}, deleted={self.deleted})"
        )


class StampStore:
    """A simple in-memory store with soft-delete and restore capabilities."""

    def __init__(self):
        self._records = []
        self._counter = 0

    def add(self, stamp):
        """Persist a stamp, assigning a fresh id."""
        self._counter += 1
        stamp.id = self._counter
        self._records.append(stamp)
        return stamp

    def find(self, stamp_id):
        """Return a stamp by id, or None when it is missing."""
        for record in self._records:
            if record.id == stamp_id:
                return record
        return None

    def delete(self, stamp_id):
        """Soft-delete a stamp: mark it without removing it from storage."""
        stamp = self.find(stamp_id)
        if stamp is None:
            raise KeyError(f"Stamp with id={stamp_id} not found")
        stamp.deleted = True
        stamp.deleted_at = datetime.now()
        return stamp

    def restore(self, stamp_id):
        """Undo a previous soft-delete for the given stamp id."""
        stamp = self.find(stamp_id)
        if stamp is None:
            raise KeyError(f"Stamp with id={stamp_id} not found")
        stamp.deleted = False
        stamp.deleted_at = None
        return stamp

    def active_stamps(self):
        """Yield only the stamps that are not soft-deleted."""
        return (stamp for stamp in self._records if not stamp.deleted)

    def all_stamps(self):
        """Yield every stored stamp, including soft-deleted ones."""
        return self._records[:]
