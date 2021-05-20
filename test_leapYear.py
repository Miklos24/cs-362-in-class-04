import unittest
from leapYear import isLeapYear

class LeapYearTest(unittest.TestCase):
    def test_valid_leap_year(self):
        self.assertTrue(isLeapYear(2004))

    def test_invalid_leap_year(self):
        self.assertFalse(isLeapYear(1300))
    
    def test_negative_leap_year(self):
        self.assertRaises(ValueError, isLeapYear, -1996)
    
    def test_string_input(self):
        self.assertRaises(TypeError, isLeapYear, "two hundred sixteen")

if __name__ == '__main__':
    unittest.main()