# === Stage 7: Генерация идентификаторов ===
# Project: StampAlbum
PROJECT_PREFIX = "SA"


def generate_unique_id(base: str) -> str:
    """Return a unique identifier with the project prefix and collision check."""
    counter = 0
    while True:
        candidate = f"{PROJECT_PREFIX}-{base}-{counter}"
        if not any(candidate == existing for existing in _ACTIVE_IDS):
            _ACTIVE_IDS.add(candidate)
            return candidate
        counter += 1


def free_identifier(base: str) -> str:
    """Return the next available identifier without registering it."""
    counter = 0
    while True:
        candidate = f"{PROJECT_PREFIX}-{base}-{counter}"
        if not any(candidate == existing for existing in _ACTIVE_IDS):
            return candidate
        counter += 1


_ACTIVE_IDS: set[str] = set()


def is_reserved(base: str) -> bool:
    """Check whether an identifier with the given base is already reserved."""
    counter = 0
    while True:
        candidate = f"{PROJECT_PREFIX}-{base}-{counter}"
        if candidate in _ACTIVE_IDS:
            return True
        counter += 1
        if counter > 10000:
            return False


def release_identifier(identifier: str) -> None:
    """Remove an identifier from the active set so it can be reused."""
    _ACTIVE_IDS.discard(identifier)


def list_reserved() -> list[str]:
    """Return a sorted list of all currently reserved identifiers."""
    return sorted(_ACTIVE_IDS)


def count_reserved() -> int:
    """Return the number of currently reserved identifiers."""
    return len(_ACTIVE_IDS)
