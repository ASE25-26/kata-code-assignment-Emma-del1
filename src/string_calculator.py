import re

from astroid.brain.brain_numpy_utils import numpy_supports_type_hints


def add(numbers: str) -> int:
    # Implementiere die String-Kalkulator-Funktion hier
    if not numbers:
        return 0
    standardDelimiter = ",|\n"

    if numbers.startswith("//"):
        parts = numbers.split("\n",1)
        delimiterPart = parts[0][2:]
        numbers = parts[1]

        if delimiterPart.startswith("[") and delimiterPart.endswith("]"):
            standardDelimiter = "|".join(re.escape(d) for d in re.findall(r"\[(.*?)\]", delimiterPart))
        else:
            standardDelimiter = re.escape(delimiterPart)

    nums = [int(n) for n in re.split(standardDelimiter, numbers)]

    neg = [n for n in nums if n < 0]
    if neg:
        raise ValueError(f"Negatives not allowed: {neg}")
    return sum(n for n in nums if n <= 1000)