# === Stage 6: Связи между сущностями ===
# Project: StampAlbum
from __future__ import annotations


class Stamp:
    def __init__(self, name: str, country: str, year: int, value: float) -> None:
        self.name = name
        self.country = country
        self.year = year
        self.value = value

    def __repr__(self) -> str:
        return f"Stamp({self.name!r}, {self.country!r}, {self.year!r}, {self.value!r})"


class Swap:
    def __init__(self, stamp: Stamp, partner: str, date: str) -> None:
        self.stamp = stamp
        self.partner = partner
        self.date = date

    def __repr__(self) -> str:
        return f"Swap({self.stamp!r}, {self.partner!r}, {self.date!r})"


class StampAlbum:
    def __init__(self) -> None:
        self.swaps: list[Swap] = []

    def add_stamp(self, name: str, country: str, year: int, value: float) -> Stamp:
        stamp = Stamp(name, country, year, value)
        self.swaps.append(stamp)
        return stamp

    def add_swap(self, stamp: Stamp, partner: str, date: str) -> Swap:
        swap = Swap(stamp, partner, date)
        self.swaps.append(swap)
        return swap

    def get_all_swaps_for_stamp(self, stamp: Stamp) -> list[Swap]:
        return [swap for swap in self.swaps if swap.stamp is stamp]

    def verify_integrity(self, stamp: Stamp) -> list[str]:
        issues: list[str] = []
        expected = self.get_all_swaps_for_stamp(stamp)
        actual = [s for s in self.swaps if s.stamp is stamp]
        if len(expected) != len(actual):
            issues.append("swap list and filter disagree")
        if not actual:
            issues.append("stamp has no swaps recorded")
        return issues

    def get_catalog_number(self, stamp: Stamp) -> int:
        swaps = self.get_all_swaps_for_stamp(stamp)
        return len(swaps)


if __name__ == "__main__":
    album = StampAlbum()
    stamp = album.add_stamp("Maple Leaf", "Canada", 1953, 1.0)
    album.add_swap(stamp, "Berlin", "2024-01-01")
    album.add_swap(stamp, "Tokyo", "2024-02-01")
    print(album.get_all_swaps_for_stamp(stamp))
    print(album.verify_integrity(stamp))
    print(album.get_catalog_number(stamp))
