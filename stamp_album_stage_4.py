# === Stage 4: Редактирование записей ===
# Project: StampAlbum
ALLOWED_STAMP_FIELDS = ("name", "country", "year", "value")


def get_stamp_by_id(stamps, stamp_id):
    for stamp in stamps:
        if stamp["id"] == stamp_id:
            return stamp
    return None


def validate_stamp_update(stamp, changes):
    if not isinstance(changes, dict):
        return None, "changes must be a dictionary"
    invalid_keys = set(changes.keys()) - set(ALLOWED_STAMP_FIELDS)
    if invalid_keys:
        return None, f"invalid fields: {sorted(invalid_keys)}"
    if "year" in changes and (not isinstance(changes["year"], int) or changes["year"] < 1):
        return None, "year must be a positive integer"
    if "value" in changes and (not isinstance(changes["value"], (int, float)) or changes["value"] <= 0):
        return None, "value must be a positive number"
    return changes, None


def update_stamp(stamps, stamp_id, changes):
    stamp = get_stamp_by_id(stamps, stamp_id)
    if stamp is None:
        return None, "stamp not found"
    validated, error = validate_stamp_update(stamp, changes)
    if error is not None:
        return None, error
    for key, value in validated.items():
        stamp[key] = value
    return stamp, None
