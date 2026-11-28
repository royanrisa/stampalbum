# === Stage 20: Общая сводка ===
# Project: StampAlbum
from collections import Counter


def summarize_stamps(stamps):
    """Return a summary dict over the given list of stamp records.

    Each stamp must be a mapping with the keys:
        'title', 'country', 'year', 'denomination'

    The result contains:
        'total'        - number of stamps
        'by_country'   - country -> count
        'latest'       - the most recent stamp record (max by year)
    """
    if not stamps:
        return {'total': 0, 'by_country': {}, 'latest': None}

    total = len(stamps)
    by_country = Counter(stamp['country'] for stamp in stamps)
    latest = max(stamps, key=lambda stamp: stamp['year'])

    return {'total': total, 'by_country': dict(by_country), 'latest': latest}
