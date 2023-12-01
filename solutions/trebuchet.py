"""Solution to Advent of Code day 1."""
import re


def decipher_calibration_document(calibration_document: list[str], text_match: bool = False) -> list[int]:
    """Deciphers the calibration document.

    The newly-improved calibration document consists of lines of text; each line originally contained a specific
    calibration value that the Elves now need to recover. On each line, the calibration value can be found by
    combining the first digit and the last digit (in that order) to form a single two-digit number.

    If text_match is specified, written numbers are taken into account as well, e.g. "one", "two", ...

    Args:
        calibration_document: A list of lines from the calibration document.
        text_match: Whether to match for written numbers as well.

    Returns:
        A list of calibration values.

    """

    calibration_values: list[int] = []
    for line in calibration_document:
        first_digit: int | None = None
        first_digit_postion: int = len(line)

        last_digit: int | None = None
        last_digit_position: int = 0

        for i, character in enumerate(line):
            try:
                first_digit: int = int(character)
                first_digit_postion: int = i
                break
            except ValueError:
                continue
        for i, character in enumerate(line[::-1]):
            try:
                last_digit: int = int(character)
                last_digit_position: int = len(line) - i - 1
                break
            except ValueError:
                continue

        if text_match:
            number_regex_string: str = r"one|two|three|four|five|six|seven|eight|nine"
            numbers: re.Pattern = re.compile(number_regex_string)
            reverse_numbers: re.Pattern = re.compile(number_regex_string[::-1])
            number_conversion: dict[str, int] = {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
            }

            if first_text_match := re.search(numbers, line):
                first_text_match_postion: int = first_text_match.span()[0]
                if first_text_match_postion < first_digit_postion:
                    first_digit: int = number_conversion[first_text_match.group()]

            if last_text_match := re.search(reverse_numbers, line[::-1]):
                last_text_match_position: int = len(line) - last_text_match.span()[1]
                if last_text_match_position > last_digit_position:
                    last_digit: int = number_conversion[last_text_match.group()[::-1]]

        calibration_values.append(int(f"{first_digit}{last_digit}"))

    return calibration_values


def main():
    """Main method."""
    with open("input_files/trebuchet.txt", "r", encoding="utf-8") as reader:
        calibration_document: list[str] = [line.rstrip("\n") for line in reader.readlines()]
    calibration_values = decipher_calibration_document(calibration_document)
    print("Part 1:")
    print(f"The sum of your calibration values is {sum(calibration_values)}.")
    print("Part 2:")
    new_calibration_values = decipher_calibration_document(calibration_document, text_match=True)
    print(f"The new sum of your calibration values is {sum(new_calibration_values)}.")


if __name__ == "__main__":
    main()
