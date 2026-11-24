# === Stage 12: Быстрые фильтры ===
# Project: StampAlbum
from datetime import date, timedelta


def is_today(stamp_date):
    return stamp_date == date.today()


def is_this_week(stamp_date):
    today = date.today()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)
    return start <= stamp_date <= end


def is_overdue(stamp_date):
    return stamp_date < date.today()


def filter_stamps(stamps, mode):
    if mode == "today":
        return [s for s in stamps if is_today(s["date"])]
    if mode == "this_week":
        return [s for s in stamps if is_this_week(s["date"])]
    if mode == "overdue":
        return [s for s in stamps if is_overdue(s["date"])]
    raise ValueError(f"Unknown filter mode: {mode}")
