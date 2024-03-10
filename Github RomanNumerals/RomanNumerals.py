class RomanNumeral:
    def __init__(self, number):
        self.number = number
        self.value = 0
        self.roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def validate(self):
        """Check if the given roman number is valid"""
        roman_numerals = self.number.upper()
        prev_value = 0

        for numeral in roman_numerals:
            if numeral not in self.roman_dict:
                raise ValueError(f"Invalid roman numeral: {numeral}")
            current_value = self.roman_dict[numeral]
            if current_value > prev_value and prev_value != 0:
                raise ValueError("Romans were not known for their subtraction...")
            prev_value = current_value

        if prev_value == 0:
            raise ValueError("Empty roman numeral")

        self.value = self._convert_to_integer()

    def _convert_to_integer(self):
        """Convert the validated roman numeral to an integer"""
        roman_numerals = self.number.upper()
        prev_value = 0
        total = 0

        for numeral in roman_numerals:
            current_value = self.roman_dict[numeral]
            if prev_value != 0 and prev_value > current_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value

        return total


def convert_roman_to_integer(roman_number):
    """Convert a roman numeral to an integer, raising a ValueError if the input is invalid"""
    roman_number = RomanNumeral(roman_number)
    roman_number.validate()
    return roman_number.value


if __name__ == "__main__":

    test_numbers = [
        "I",
        "III",
        "IIII",
        "IV",
        "VV",
        "X",
        "C",
        "M",
        "MC",
        "MMX",
        "MMMCC"
    ]
    test_numbers1 = [
        "MMMXCLXXIV",
        "IIVVMM",
        "MCMLXXIX",
        "MCMXLIV",
        "MMXVI",
        "MMMCCIII",
        "INVALID"
    ]

    for number in test_numbers:
        try:
            print(f"{number}: {convert_roman_to_integer(number)}")
        except ValueError as e:
            print(f"{number}: Error - {str(e)}")


    for number in test_numbers1:
        try:
            print(f"{number}: {convert_roman_to_integer(number)}")
        except ValueError as e:
            print(f"{number}: Error - {str(e)}")