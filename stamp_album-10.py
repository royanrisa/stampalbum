# === Stage 10: Группировка ===
# Project: StampAlbum
from collections import Counter


def group_stamps_by_country(stamps):
    countries = Counter()
    for stamp in stamps:
        countries[stamp["country"]] += 1
    return dict(sorted(countries.items(), key=lambda kv: kv[0]))


def group_stamps_by_country_with_counts(stamps):
    groups = {}
    for stamp in stamps:
        country = stamp["country"]
        groups.setdefault(country, []).append(stamp)
    counts = {country: len(group) for country, group in groups.items()}
    return groups, counts


def count_stamps_by_country(stamps):
    counts = Counter(stamp["country"] for stamp in stamps)
    return dict(sorted(counts.items(), key=lambda kv: kv[0]))


def summarize_by_country(stamps):
    result = {}
    for stamp in stamps:
        country = stamp["country"]
        entry = result.setdefault(country, {"count": 0, "stamps": []})
        entry["count"] += 1
        entry["stamps"].append(stamp)
    return result


def group_and_count(stamps):
    grouped = {}
    counts = {}
    for stamp in stamps:
        country = stamp["country"]
        grouped.setdefault(country, []).append(stamp)
        counts[country] = counts.get(country, 0) + 1
    return grouped, counts


if __name__ == "__main__":
    sample_stamps = [
        {"name": "Rose", "country": "USA", "year": 1900, "value": 0.05},
        {"name": "Eagle", "country": "USA", "year": 1910, "value": 0.10},
        {"name": "Tulip", "country": "Netherlands", "year": 1920, "value": 0.20},
        {"name": "Lion", "country": "England", "year": 1930, "value": 0.30},
        {"name": "Sunflower", "country": "Netherlands", "year": 1940, "value": 0.50},
    ]

    print("Grouped by country:")
    for country, group in group_stamps_by_country(sample_stamps).items():
        print(f"  {country}: {len(group)} stamps")

    print("\nCounts by country:")
    for country, count in count_stamps_by_country(sample_stamps).items():
        print(f"  {country}: {count}")

    print("\nSummary by country:")
    for country, entry in summarize_by_country(sample_stamps).items():
        print(f"  {country}: {entry['count']} stamps")
