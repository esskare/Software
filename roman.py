import unittest
class Roman:
    def __init__(self):
        self.map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, s):
        if len(s) == 1:
            # Handle single-letter input
            single_letter = s[0]
            if single_letter not in self.map:
                print("Invalid")
                return -1  # or any other value indicating invalid input
            return self.map[single_letter]

        converted_number = 0
        for i in range(len(s)):
            current_number = self.map[s[i]]
            next_num = self.map[s[i + 1]] if i + 1 < len(s) else 0
            if current_number >= next_num:
                converted_number += current_number
            else:
                converted_number -= current_number
        return converted_number

def main():
    # Get user input for a Roman numeral
    user_input = input("Enter a Roman numeral: ")

    # Test the Roman class with user input
    roman_numeral = Roman()
    result = roman_numeral.roman_to_int(user_input)

    # Output the result
    if result == -1:
        print("Invalid input. Please enter a valid Roman numeral.")
    else:
        print("Roman to Integer:", result)

if __name__ == "__main__":
    main()


class TestRomanConversion(unittest.TestCase):

    def setUp(self):
        self.roman_converter = Roman()

    def test_single_letter_conversion(self):
        self.assertEqual(self.roman_converter.roman_to_int('I'), 1)
        self.assertEqual(self.roman_converter.roman_to_int('V'), 5)
        # Add more single-letter conversion tests as needed

    def test_multiple_letters_conversion(self):
        self.assertEqual(self.roman_converter.roman_to_int('IX'), 9)
        self.assertEqual(self.roman_converter.roman_to_int('XXI'), 21)
        # Add more multiple-letter conversion tests as needed

    def test_invalid_input(self):
        self.assertEqual(self.roman_converter.roman_to_int('INVALID'), -1)
        # Add more invalid input tests as needed

if __name__ == '__main__':
    unittest.main()
