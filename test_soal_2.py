import unittest
from soal_2 import IndonesianChangeCalculator


class TestIndonesianChangeCalculator(unittest.TestCase):

    def setUp(self):
        """
        Set up a fresh calculator for each test case.
        """
        self.calculator = IndonesianChangeCalculator()

    def print_test_case(self, total_cost, amount_paid, change, change_details):
        """
        Utility function to print test case input and output in the specified format.
        """
        print(f"Input:\nTotal belanja seorang customer: Rp {total_cost:,}")
        print(f"Pembeli membayar: Rp {amount_paid:,}")

        if change is False:
            print("Output:\nFalse, kurang bayar")
        else:
            rounded_change = (change // 100) * 100
            print(f"Output:\nKembalian yang harus diberikan kasir: {change:,}, dibulatkan menjadi {rounded_change:,}")
            print("Pecahan uang:")
            for denomination, count in change_details.items():
                unit = "lembar" if denomination >= 1000 else "koin"
                print(f"{count} {unit}(s) of Rp {denomination:,}")

    def test_case_1(self):
        """
        Test case 1: Total cost Rp 700,649, Amount paid Rp 800,000
        """
        total_cost = 700649
        amount_paid = 800000
        expected_change = 99351
        expected_details = {
            50000: 1,
            20000: 2,
            5000: 1,
            2000: 2,
            200: 1,
            100: 1
        }

        change, change_details = self.calculator.calculate_change(total_cost, amount_paid)
        self.print_test_case(total_cost, amount_paid, change, change_details)
        self.assertEqual(change, expected_change)
        self.assertEqual(change_details, expected_details)

    def test_case_2(self):
        """
        Test case 2: Total cost Rp 575,650, Amount paid Rp 580,000
        """
        total_cost = 575650
        amount_paid = 580000
        expected_change = 4350
        expected_details = {
            2000: 2,
            200: 1,
            100: 1
        }

        change, change_details = self.calculator.calculate_change(total_cost, amount_paid)
        self.print_test_case(total_cost, amount_paid, change, change_details)
        self.assertEqual(change, expected_change)
        self.assertEqual(change_details, expected_details)

    def test_case_3(self):
        """
        Test case 3: Total cost Rp 657,650, Amount paid Rp 600,000
        """
        total_cost = 657650
        amount_paid = 600000

        result = self.calculator.calculate_change(total_cost, amount_paid)
        self.print_test_case(total_cost, amount_paid, result, {})
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
