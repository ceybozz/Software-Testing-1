
import unittest
import leapyear

class AbcTest(unittest.TestCase):
    # Abc unittest code here
    def test_Blank(self):
        # to_leap_year should fail with blank string
        self.assertRaises(leapyear.leapYearError, leapyear.to_leap_year, '')

    def test_string(self):
        # to_leap_year should fail with string input
        self.assertRaises(leapyear.leapYearError,leapyear.to_leap_year,'t')

class XyzTest(unittest.TestCase):
    def test_negative(self):
        # to_leap_year should fail with negative input
        self.assertRaises(leapyear.RangeError, leapyear.to_leap_year, -1,)

    def test_non_integer(self):
        # to_leap_year should fail with non-integer input
        self.assertRaises(leapyear.IntError, leapyear.to_leap_year, 0.5)

if __name__ == '__main__':
    unittest.main()
