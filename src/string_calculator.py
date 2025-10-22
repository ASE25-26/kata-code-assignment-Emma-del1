import re


def add(numbers: str) -> int:
    # Implementiere die String-Kalkulator-Funktion hier
    if not numbers:
        return 0
    standard_delimiter = ",|\n"

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter_part = parts[0][2:]
        numbers = parts[1]

        if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
            standard_delimiter = "|".join(
                re.escape(d) for d in re.findall(r"\[(.*?)\]", delimiter_part))
        else:
            standard_delimiter = re.escape(delimiter_part)

    nums = [int(n) for n in re.split(standard_delimiter, numbers)]

    neg = [n for n in nums if n < 0]
    if neg:
        raise ValueError(f"Negatives not allowed: {neg}")
    return sum(n for n in nums if n <= 1000)
