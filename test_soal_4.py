import unittest
from datetime import datetime
from soal_4 import LeavePolicy, LeaveChecker

class TestLeaveChecker(unittest.TestCase):

    def setUp(self):
        # Set up the leave policy and leave checker
        self.leave_policy = LeavePolicy()  # Default 14 days leave and max 3 consecutive leave
        self.leave_checker = LeaveChecker(self.leave_policy)

    def test_case_1(self):
        """
        Test Case 1:
        Input:
        - Public holidays = 7
        - Join date = 2021-05-01
        - Plan leave date = 2021-07-05
        - Leave duration = 1
        Output:
        - False
        - Alasan: Karena belum 180 hari sejak tanggal join karyawan
        """
        can_take, reason = self.leave_checker.can_take_leave("2021-05-01", "2021-07-05", 1, 7)
        self.assertFalse(can_take)
        self.assertEqual(reason, "Belum 180 hari sejak tanggal join karyawan.")

    def test_case_2(self):
        """
        Test Case 2:
        Input:
        - Public holidays = 7
        - Join date = 2021-05-01
        - Plan leave date = 2021-11-05
        - Leave duration = 3
        Output:
        - False
        - Alasan: Karena hanya boleh mengambil 1 hari cuti
        """
        can_take, reason = self.leave_checker.can_take_leave("2021-05-01", "2021-11-05", 3, 7)
        self.assertFalse(can_take)
        self.assertEqual(reason, "Hanya boleh mengambil 1 hari cuti.")

    def test_case_3(self):
        """
        Test Case 3:
        Input:
        - Public holidays = 7
        - Join date = 2021-01-05
        - Plan leave date = 2021-12-18
        - Leave duration = 1
        Output:
        - True
        """
        can_take, reason = self.leave_checker.can_take_leave("2021-01-05", "2021-12-18", 1, 7)
        self.assertTrue(can_take)
        self.assertEqual(reason, "Boleh mengambil cuti.")

    def test_case_4(self):
        """
        Test Case 4:
        Input:
        - Public holidays = 7
        - Join date = 2021-01-05
        - Plan leave date = 2021-12-18
        - Leave duration = 3
        Output:
        - True
        """
        can_take, reason = self.leave_checker.can_take_leave("2021-01-05", "2021-12-18", 3, 7)
        self.assertTrue(can_take)
        self.assertEqual(reason, "Boleh mengambil cuti.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
