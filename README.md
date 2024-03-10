# Roman to Interger Converter
The code need to have a RomanNumeral class and a convert_roman_to_integer function to convert Roman numerals to integers. The code includes validation to ensure the input Roman numerals are valid.

Here's a brief overview of how the code works:

RomanNumeral class: This class has two methods, validate and _convert_to_integer.

validate: This method checks if the given Roman numeral is valid. It iterates through the numerals, comparing their values and ensuring that a smaller numeral does not precede a larger one (except for special cases like IV, where a smaller numeral can precede a larger one). If the Roman numeral is invalid, it raises a ValueError.
_convert_to_integer: This method converts a validated Roman numeral to an integer. It iterates through the numerals and accumulates their integer values.
convert_roman_to_integer function: This function takes a Roman numeral as input, creates a RomanNumeral object, and calls the validate method. If the Roman numeral is valid, it returns the integer value; otherwise, it raises a ValueError.

To test the code, you can run the script, which will output the integer values of the provided test cases. If a Roman numeral is invalid, it will print an error message.

For example:

"I": 1
"III": 3
"IV": 4
"INVALID": Error - Invalid roman numeral
To further test the code, you can add more test cases to the test_numbers and test_numbers1 lists. Make sure to include a variety of valid and invalid Roman numerals to ensure the code handles different edge cases.
