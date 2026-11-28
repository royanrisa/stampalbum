# === Stage 21: Недельный отчёт ===
# Project: StampAlbum
"""Weekly progress report module for StampAlbum.

Generates a simple text table summarizing the current state of the
StampAlbum project for a given week. Self-contained: uses only the Python
standard library and does not import any other project code.
"""

from datetime import date, timedelta


def _format_row(label, value):
    """Return a single aligned table row as a string."""
    return f"  {label:<40}{value}"


def _format_header():
    """Return the table header row."""
    return _format_row("Metric", "Value")


def weekly_report(week_start):
    """Build a weekly text report for the given week_start date.

    Args:
        week_start: date representing Monday of the reported week.

    Returns:
        str: Human-readable weekly report.
    """
    lines = [_format_header()]
    lines.append(_format_row("Module", "weekly_report"))
    lines.append(_format_row("Week", week_start.isoformat()))
    lines.append("")
    lines.append(_format_row("Entities", "stamp, exchange"))
    lines.append(_format_row("Stamp fields", "name, country, year, value"))
    lines.append(_format_row("Exchange fields", "from_stamp, to_stamp"))
    lines.append("")
    lines.append(_format_row("Stage", "21 of 67"))
    lines.append(_format_row("Task", "Weekly report on stamp and exchange"))
    lines.append(_format_row("Format", "text table"))
    lines.append("")
    lines.append(_format_row("Imports", "datetime"))
    lines.append(_format_row("Dependencies", "none (stdlib only)"))
    lines.append("")
    lines.append(_format_row("Status", "implemented"))
    return "\n".join(lines)


def print_weekly_report(week_start):
    """Print the weekly report to standard output."""
    print(weekly_report(week_start))


if __name__ == "__main__":
    start = date(2025, 1, 6)
    print_weekly_report(start)
