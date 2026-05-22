"""Functions for determining Armstrong numbers."""

def is_armstrong_number(number):
    """Determine wether a number is an Armstrong number."""
    digits = str(number)
    power = len(digits)

    total = 0

    for digit in digits:
        total += int(digit) ** power


    return total == number
