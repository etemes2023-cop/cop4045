"""Utilities for reading weather-station observations."""

import csv
import math
import sys
from datetime import datetime


def _parse_date(value: str) -> datetime:
    """Convert a supported date string to a ``datetime`` object.

    Observation files normally use ISO dates, but the two common slash-based
    formats are also accepted.  A ``ValueError`` signals an invalid date.
    """
    for date_format in ("%Y-%m-%d", "%m/%d/%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(value, date_format)
        except ValueError:
            pass
    raise ValueError("invalid date")


def read_observations(filename: str) -> tuple[dict[str, list[tuple[datetime, float]]], list[tuple[int, str]]]:
    """Read ``station,date,temperature`` observations from a CSV file.

    Returns a pair ``(observations, errors)``.  Dates are stored as
    :class:`datetime.datetime` objects, each station's observations are sorted
    chronologically, and invalid rows are recorded rather than added.
    """
    observations: dict[str, list[tuple[datetime, float]]] = {}
    errors: list[tuple[int, str]] = []
    seen: set[tuple[str, datetime]] = set()

    with open(filename, "r", newline="", encoding="utf-8") as observation_file:
        reader = csv.reader(observation_file)
        for line_number, row in enumerate(reader, start=1):
            # Exactly three nonempty fields are required: station, date, temp.
            if len(row) != 3 or any(not field.strip() for field in row):
                errors.append((line_number, "malformed line"))
                continue

            station, date_text, temperature_text = (field.strip() for field in row)
            try:
                date = _parse_date(date_text)
            except ValueError:
                errors.append((line_number, "malformed line"))
                continue

            try:
                temperature = float(temperature_text)
                if not math.isfinite(temperature):
                    raise ValueError
            except ValueError:
                errors.append((line_number, "invalid temperature"))
                continue

            key = (station, date)
            if key in seen:
                errors.append((line_number, "duplicate station/date combination"))
                continue

            seen.add(key)
            observations.setdefault(station, []).append((date, temperature))

    for station_observations in observations.values():
        station_observations.sort(key=lambda observation: observation[0])

    return observations, errors


def station_statistics(observations: dict[str, list[tuple[datetime, float]]]) -> dict[str, tuple[float, float, float]]:
    """Return each station's minimum, maximum, and mean temperature.

    The result maps a station name to ``(minimum, maximum, mean)``.
    Stations with no observations are omitted because those statistics are not
    defined.
    """
    statistics: dict[str, tuple[float, float, float]] = {}

    for station, station_observations in observations.items():
        if not station_observations:
            continue

        temperatures = [temperature for _, temperature in station_observations]
        statistics[station] = (
            min(temperatures),
            max(temperatures),
            sum(temperatures) / len(temperatures),
        )

    return statistics


def station_outliers(observations: dict[str, list[tuple[datetime, float]]]) -> dict[str, tuple[datetime, float, float]]:
    """Return stations whose latest temperature is greater than their mean.

    Each result value is ``(date, temperature, mean)``.  Observation lists
    produced by :func:`read_observations` are ordered by date, so their final
    item is the latest report.
    """
    statistics = station_statistics(observations)

    return {
        station: (
            station_observations[-1][0],
            station_observations[-1][1],
            statistics[station][2],
        )
        for station, station_observations in observations.items()
        if station_observations
        and station_observations[-1][1] > statistics[station][2]
    }


def write_statistics(filename: str, statistics: dict[str, tuple[float, float, float]]) -> None:
    """Write station statistics as sorted CSV rows.

    Each row has the form ``station,minimum,maximum,mean``.  Station names
    are written in lexicographic order and all numeric fields use one decimal
    place.
    """
    with open(filename, "w", newline="", encoding="utf-8") as statistics_file:
        writer = csv.writer(statistics_file)
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]
            writer.writerow(
                [station, f"{minimum:.1f}", f"{maximum:.1f}", f"{mean:.1f}"]
            )


def main() -> None:
    """Read observations and write their statistics from command-line files.

    Usage: ``python p5_Temes_Enrique.py observations.csv statistics.csv``
    """
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <observation_file> <output_file>")
        return

    observation_filename, output_filename = sys.argv[1:]
    try:
        observations, errors = read_observations(observation_filename)
    except OSError as error:
        print(f"Could not read '{observation_filename}': {error}")
        return

    statistics = station_statistics(observations)
    outliers = station_outliers(observations)

    print("Statistics:")
    for station in sorted(statistics):
        minimum, maximum, mean = statistics[station]
        print(f"{station}: min={minimum:.1f}, max={maximum:.1f}, mean={mean:.1f}")

    print("Outliers:")
    for station in sorted(outliers):
        date, temperature, mean = outliers[station]
        print(f"{station}: {date:%Y-%m-%d}, {temperature:.1f}, mean={mean:.1f}")

    if errors:
        print("Input errors:")
        for line_number, message in errors:
            print(f"Line {line_number}: {message}")

    try:
        write_statistics(output_filename, statistics)
    except OSError as error:
        print(f"Could not write '{output_filename}': {error}")


if __name__ == "__main__":
    main()
