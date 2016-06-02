from app import is_leap_year

import unittest

class TestIsLeapYear(unittest.TestCase):
    def setUp(self):
        self.leapYear = 1996
        self.nonLeapYear = 2001
        self.millenialYear = 2000
        self.oddCenturyYear = 1900

    def tearDown(self):
        pass

    def test_leap_year_returns_true(self):
        self.assertEqual(is_leap_year(self.leapYear), True)

    def test_non_leap_year_returns_false(self):
        self.assertEqual(is_leap_year(self.nonLeapYear), False)

    def test_millenial_year_is_leap_year(self):
        self.assertEqual(is_leap_year(self.millenialYear), True)

    def test_odd_turn_of_century_is_not_leap_year(self):
        self.assertEqual(is_leap_year(self.oddCenturyYear), False)

if __name__ == '__main__':
    unittest.main()
