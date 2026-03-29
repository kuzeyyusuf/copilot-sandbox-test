def average_ratios(numbers):
    """Compute the average of 100 divided by each non-zero number in ``numbers``.

    Zero values are skipped to avoid division-by-zero errors. A ``ValueError``
    is raised if there are no non-zero numeric values or if a non-numeric
    element is encountered.
    """
    total = 0.0
    count = 0
    for n in numbers:
        try:
            num = float(n)
        except (TypeError, ValueError):
            raise ValueError(f"Non-numeric value encountered: {n!r}")
        if num == 0.0:
            # skip zeros instead of dividing
            continue
        total += 100.0 / num
        count += 1

    if count == 0:
        raise ValueError("No non-zero numeric values to compute average ratios.")

    return total / count


if __name__ == "__main__":
    print(average_ratios([10, 5, 0]))
