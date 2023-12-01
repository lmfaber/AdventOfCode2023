import pytest

from solutions.trebuchet import decipher_calibration_document


class TestTrebuchet:
    @pytest.mark.parametrize(
        "calibration_document, calibration_values, text_match",
        [
            (["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], [12, 38, 15, 77], False),
            (
                [
                    "two1nine",
                    "eightwothree",
                    "abcone2threexyz",
                    "xtwone3four",
                    "4nineeightseven2",
                    "zoneight234",
                    "7pqrstsixteen",
                    "7oneight",
                ],
                [29, 83, 13, 24, 42, 14, 76, 78],
                True,
            ),
        ],
    )
    def test_decipher_calibration_document(
        self, calibration_document: list[str], calibration_values: list[int], text_match: bool
    ):
        assert decipher_calibration_document(calibration_document, text_match) == calibration_values
