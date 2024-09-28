import unittest

from soal_3 import *

import unittest

import unittest

class TestBracketValidator(unittest.TestCase):
    def test_valid_strings(self):
        valid_inputs = [
            "{{[<>[{{}}]]}}",
            "{<{[[{{[]<{{[{[]<>}]}}<>>}}]]}>}",
            "{{[{<[[{<{<<<[{{{[]{<{[<[[<{{[[[[[<{[{<[<<[[<<{[[{[<<"
            "<<<<<[{[{[{{<{[[<{<<<{<{[<>]}>}>>[]>}>]]}>}}]}]}]>>>>>>"
            ">]}]]}>>]]>>]>}]}>]]]]]}}>]]>]}>}}}}]>>>}>}]]>}]}}",
            "[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{["
            "{{[{{{{[<<{{{<{[{[[[{<<<[{[<{<<<>>>}>]}]>>>}]]]}]}>}}"
            "}>>]}}}}]}}]}>]>}>}>}}>>]}}>]>]]]>>>]}}>]]]>]>]}}>]>]"
            "]]}]}>}>]",
            "[[{[[<{{{{[[[<[{[[<{{{{[{[{[[[<<{<{[{<<<[[<[{[<{{["
            "{[<[[<<[{<<[[[{<[{[[{{<<>[<<{{<<{[[[<{}{[{{{[[{{[[<[{}]"
            ">]]}}]]}}}]}>]]]}>>}}>>]>}}]]}]>}]]]>>}]>>]]>]}]}}>]}]>"
            "]]>>>}]}>}>>]]]}]}]}}}}>]]}]>]]]}}}}>]]}]]",
            "{}<>"
        ]
        for input_str in valid_inputs:
            with self.subTest(input=input_str):
                print(f"Testing valid input: {input_str}")
                self.assertTrue(validate_string(input_str), f"Failed for input: {input_str}")

    def test_invalid_strings(self):
        invalid_inputs = [
            "]",
            "][",
            "[>]",
            "[>",
            "{}<[>]"
        ]
        for input_str in invalid_inputs:
            with self.subTest(input=input_str):
                print(f"Testing invalid input: {input_str}")
                self.assertFalse(validate_string(input_str), f"Failed for input: {input_str}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
