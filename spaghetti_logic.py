from typing import Iterable, List


def calculate_totals(values: Iterable[float], multiplier: float = 1.15) -> List[float]:
    """Return a list of totals by applying ``multiplier`` to each numeric value in ``values``.

    Raises ``ValueError`` if a non-numeric value is encountered.
    """
    totals: List[float] = []
    for v in values:
        try:
            num = float(v)
        except (TypeError, ValueError):
            raise ValueError(f"Non-numeric value encountered: {v!r}")
        totals.append(num * multiplier)
    return totals


def format_total(value: float) -> str:
    """Return a formatted string for a total value.

    Example: 123.456 -> "Total: 123.46"
    """
    return f"Total: {value:.2f}"


def append_log(values: Iterable[float], path: str = "log.txt") -> None:
    """Append the provided values (as a list) to the log file at ``path``.

    This keeps the original behavior of appending a simple stringified list.
    """
    with open(path, "a") as f:
        f.write(str(list(values)) + "\n")


def process_data(data: Iterable[float], multiplier: float = 1.15, log_path: str = "log.txt") -> List[float]:
    """Process numeric ``data`` by calculating totals, printing formatted totals,
    appending the totals to a log file, and returning the totals.

    Keeps the original behavior but with clearer structure and parameterization.
    """
    totals = calculate_totals(data, multiplier=multiplier)
    for total in totals:
        print(format_total(total))
    append_log(totals, path=log_path)
    return totals
