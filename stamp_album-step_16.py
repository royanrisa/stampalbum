# === Stage 16: Избранное ===
# Project: StampAlbum
from typing import List, Dict, Optional

class Stamp:
    def __init__(self, name: str, country: str, year: int, value: float):
        self.name = name
        self.country = country
        self.year = year
        self.value = value
        self.favorited = False

    def toggle_favorite(self) -> None:
        self.favorited = not self.favorited

    def is_favorited(self) -> bool:
        return self.favorited


def add_favorite(stamps: List[Stamp], stamp: Stamp) -> None:
    stamp.toggle_favorite()


def remove_favorite(stamps: List[Stamp], stamp: Stamp) -> None:
    stamp.toggle_favorite()


def get_favorited(stamps: List[Stamp]) -> List[Stamp]:
    return [s for s in stamps if s.is_favorited()]


def print_favorite_list(stamps: List[Stamp]) -> None:
    favorites = get_favorited(stamps)
    if not favorites:
        print("No favorites added.")
        return
    print("Favorite stamps:")
    for stamp in favorites:
        print(f"  - {stamp.name} ({stamp.country}, {stamp.year})")


def is_favorited(stamps: List[Stamp], stamp_name: str) -> bool:
    for stamp in stamps:
        if stamp.name == stamp_name and stamp.is_favorited():
            return True
    return False


def favorite_count(stamps: List[Stamp]) -> int:
    return len(get_favorited(stamps))
