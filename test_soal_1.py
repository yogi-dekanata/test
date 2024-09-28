import unittest
from soal_1 import CaseInsensitiveComparator, StringMatcher

class TestStringMatcher(unittest.TestCase):
    def setUp(self):
        """
        Set up a fresh comparator and matcher for each test case.
        """
        self.comparator = CaseInsensitiveComparator()
        self.matcher = StringMatcher(self.comparator)

    def print_test_case(self, input_list, result):
        """
        Utility function to print test case input and output in the specified format.
        """
        print(f"Contoh input:\n{len(input_list)}")
        for string in input_list:
            print(string)
        if result:
            print(f"Contoh output: {' '.join(map(str, result))}")
        else:
            print("Contoh output: false")

    def test_case_1(self):
        """
        Test case 1: Matching strings in list
        """
        input_list = ["abcd", "acbd", "aaab", "acbd"]
        expected_output = [2, 4]
        result = self.matcher.find_first_matching_set(input_list)
        self.print_test_case(input_list, result)
        self.assertEqual(result, expected_output)

    def test_case_2(self):
        """
        Test case 2: Multiple matching strings in a larger list
        """
        input_list = ["Satu", "Sate", "Tujuh", "Tusuk", "Tujuh", "Sate", "Bonus", "Tiga", "Puluh", "Tujuh", "Tusuk"]
        expected_output = [2, 6]  # Indeks string "Sate" yang benar karena lebih dahulu di temukan
        result = self.matcher.find_first_matching_set(input_list)
        self.print_test_case(input_list, result)
        self.assertEqual(result, expected_output)

    def test_case_3(self):
        """
        Test case 3: No matching strings in list
        """
        input_list = ["pisang", "goreng", "enak", "sekali", "rasanya"]
        expected_output = False
        result = self.matcher.find_first_matching_set(input_list)
        self.print_test_case(input_list, result)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
