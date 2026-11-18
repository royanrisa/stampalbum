# === Stage 1: Каркас модуля ===
# Project: StampAlbum
from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Stamp:
    name: str
    country: str
    year: int
    denomination: float


def create_demo_stamps() -> List[Stamp]:
    return [
        Stamp(name="Liberty Bell", country="USA", year=1918, denomination=1.0),
        Stamp(name="Cranach", country="Germany", year=1928, denomination=1.0),
        Stamp(name="Beylerbey", country="Egypt", year=1909, denomination=0.5),
        Stamp(name="Marianne", country="France", year=1903, denomination=0.2),
    ]


def main() -> None:
    stamps: List[Stamp] = create_demo_stamps()
    print("StampAlbum - Welcome")
    print(f"Total stamps: {len(stamps)}")
    for stamp in stamps:
        print(f"{stamp.name} ({stamp.country}, {stamp.year}, {stamp.denomination})")


if __name__ == "__main__":
    main()
