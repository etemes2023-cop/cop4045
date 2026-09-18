"""Tests for the weather-station observation utilities."""

from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from Homework2.p5_Temes_Enrique import (
    read_observations,
    station_outliers,
    station_statistics,
    write_statistics,
)


class ObservationTests(unittest.TestCase):
    """Exercise valid data, rejected rows, calculations, and file output."""

    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.directory = Path(self.temporary_directory.name)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def make_observation_file(self, contents: str) -> Path:
        filename = self.directory / "observations.csv"
        filename.write_text(contents, encoding="utf-8")
        return filename

    def test_reads_multiple_stations_and_sorts_dates(self) -> None:
        filename = self.make_observation_file(
            "Orlando,2025-03-02,78.0\nMiami,2025-03-01,81.0\n"
            "Orlando,2025-03-01,70.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(errors, [])
        self.assertEqual(set(observations), {"Miami", "Orlando"})
        self.assertEqual(
            observations["Orlando"],
            [(datetime(2025, 3, 1), 70.0), (datetime(2025, 3, 2), 78.0)],
        )

    def test_preserves_negative_temperatures(self) -> None:
        filename = self.make_observation_file("Anchorage,2025-01-01,-12.5\n")

        observations, errors = read_observations(filename)

        self.assertEqual(errors, [])
        self.assertEqual(observations["Anchorage"], [(datetime(2025, 1, 1), -12.5)])

    def test_rejects_duplicate_station_date(self) -> None:
        filename = self.make_observation_file(
            "Miami,2025-01-01,70.0\nMiami,2025-01-01,72.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(observations["Miami"], [(datetime(2025, 1, 1), 70.0)])
        self.assertEqual(errors, [(2, "duplicate station/date combination")])

    def test_rejects_invalid_temperature_and_date_range(self) -> None:
        filename = self.make_observation_file(
            "Tampa,2025-01-01,not-a-number\nTampa,2025-02-30,75.0\n"
        )

        observations, errors = read_observations(filename)

        self.assertEqual(observations, {})
        self.assertEqual(
            errors,
            [(1, "invalid temperature"), (2, "malformed line")],
        )

    def test_calculates_station_statistics(self) -> None:
        observations = {
            "Miami": [(datetime(2025, 1, 1), 60.0), (datetime(2025, 1, 2), 90.0)],
            "Orlando": [(datetime(2025, 1, 1), -4.0), (datetime(2025, 1, 2), 2.0)],
        }

        self.assertEqual(
            station_statistics(observations),
            {"Miami": (60.0, 90.0, 75.0), "Orlando": (-4.0, 2.0, -1.0)},
        )

    def test_identifies_stations_with_latest_temperature_above_mean(self) -> None:
        observations = {
            "Miami": [(datetime(2025, 1, 1), 60.0), (datetime(2025, 1, 2), 90.0)],
            "Orlando": [(datetime(2025, 1, 1), 80.0), (datetime(2025, 1, 2), 70.0)],
        }

        self.assertEqual(
            station_outliers(observations),
            {"Miami": (datetime(2025, 1, 2), 90.0, 75.0)},
        )

    def test_writes_sorted_statistics_with_one_decimal_place(self) -> None:
        filename = self.directory / "statistics.csv"
        write_statistics(
            filename,
            {"Zebra": (-1, 2, 0.5), "Alpha": (3, 8, 5.25)},
        )

        self.assertEqual(
            filename.read_text(encoding="utf-8"),
            "Alpha,3.0,8.0,5.2\nZebra,-1.0,2.0,0.5\n",
        )

    def test_missing_file_raises_file_not_found_error(self) -> None:
        missing_filename = self.directory / "does-not-exist.csv"

        with self.assertRaises(FileNotFoundError):
            read_observations(missing_filename)


if __name__ == "__main__":
    unittest.main()
