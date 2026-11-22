# === Stage 8: Фильтрация записей ===
# Project: StampAlbum
from bisect import bisect_left, bisect_right


def filter_stamps_by_country(stamps, country):
    return [s for s in stamps if s["country"] == country]


def filter_stamps_by_year_range(stamps, year_start, year_end):
    return [s for s in stamps if year_start <= s["year"] <= year_end]


def filter_stamps_by_country_and_year_range(stamps, country, year_start, year_end):
    result = filter_stamps_by_country(stamps, country)
    return filter_stamps_by_year_range(result, year_start, year_end)


def sorted_stamps_by_year(stamps):
    return sorted(stamps, key=lambda s: s["year"])


def find_year_bounds(stamps, year):
    sorted_stamps = sorted_stamps_by_year(stamps)
    indices = [bisect_left(sorted_stamps, {"year": year}),
               bisect_right(sorted_stamps, {"year": year})]
    return indices


def filter_stamps_by_country_and_year_range_bisect(stamps, country, year_start, year_end):
    country_sorted = sorted_stamps_by_year(filter_stamps_by_country(stamps, country))
    start = bisect_left(country_sorted, {"year": year_start})
    end = bisect_right(country_sorted, {"year": year_end})
    return country_sorted[start:end]


def get_unique_countries(stamps):
    return sorted(set(s["country"] for s in stamps))


def get_years_by_country(stamps, country):
    country_stamps = filter_stamps_by_country(stamps, country)
    years = [s["year"] for s in country_stamps]
    return sorted(set(years))


def get_year_ranges_by_country(stamps, country):
    years = get_years_by_country(stamps, country)
    if not years:
        return []
    return [{"start": years[0], "end": years[-1]}]
