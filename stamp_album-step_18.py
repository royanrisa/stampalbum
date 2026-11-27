# === Stage 18: История изменений ===
# Project: StampAlbum
from datetime import datetime


class StampHistoryEntry:
    """A single change record for a stamp."""

    def __init__(self, changed_at, field, old_value, new_value):
        self.changed_at = changed_at
        self.field = field
        self.old_value = old_value
        self.new_value = new_value

    def __repr__(self):
        return (
            f"StampHistoryEntry(changed_at={self.changed_at!r}, "
            f"field={self.field!r}, old_value={self.old_value!r}, "
            f"new_value={self.new_value!r})"
        )


class StampHistory:
    """Stores the change history for a stamp in a list of entries."""

    def __init__(self):
        self._entries = []

    def add(self, changed_at, field, old_value, new_value):
        entry = StampHistoryEntry(changed_at, field, old_value, new_value)
        self._entries.append(entry)
        return entry

    def get(self, index):
        return self._entries[index]

    def get_last(self):
        return self._entries[-1] if self._entries else None

    def count(self):
        return len(self._entries)

    def __len__(self):
        return len(self._entries)

    def __iter__(self):
        return iter(self._entries)

    def __repr__(self):
        return f"StampHistory(entries={self._entries!r})"
