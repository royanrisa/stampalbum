# === Stage 11: Постраничный вывод ===
# Project: StampAlbum
from typing import List, Dict, Any, Optional

PAGE_SIZE = 20

class StampPage:
    def __init__(self, page: int, size: int, stamps: List[Dict[str, Any]]):
        self.page = page
        self.size = size
        self.stamps = stamps

    def total_pages(self, total: int) -> int:
        return (total + self.size - 1) // self.size

    def has_next(self) -> bool:
        return self.page < self.total_pages(len(self.stamps))

    def has_prev(self) -> bool:
        return self.page > 0

    def current_offset(self) -> int:
        return self.page * self.size

    def remaining(self) -> int:
        return len(self.stamps) - self.current_offset()


def paginate(stamps: List[Dict[str, Any]], page: int = 0, size: int = PAGE_SIZE) -> StampPage:
    page = max(0, min(page, stamps.total_pages() - 1 if hasattr(stamps, "total_pages") else 0))
    size = max(1, size)
    start = page * size
    end = start + size
    return StampPage(page, size, stamps[start:end])


class StampCollection:
    def __init__(self, stamps: List[Dict[str, Any]]):
        self.stamps = stamps

    def __len__(self) -> int:
        return len(self.stamps)

    def total_pages(self, size: int = PAGE_SIZE) -> int:
        return (len(self.stamps) + size - 1) // size

    def page(self, page: int = 0, size: int = PAGE_SIZE) -> StampPage:
        page = max(0, min(page, self.total_pages(size) - 1))
        size = max(1, size)
        start = page * size
        end = start + size
        return StampPage(page, size, self.stamps[start:end])


def build_page_info(page: int, total_pages: int) -> Dict[str, Any]:
    return {
        "page": page,
        "total_pages": total_pages,
        "has_next": page < total_pages - 1,
        "has_prev": page > 0,
    }
