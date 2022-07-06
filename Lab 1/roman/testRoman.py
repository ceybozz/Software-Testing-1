import roman
import unittest

class KnownValues(unittest.TestCase): 
    known_roman = ( (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), 
    (10, 'X'), (50, 'L'), (100, 'C'), (500, 'D'), (1000, 'M'), (31, 'XXXI'), (148, 'CXLVIII'), (294, 'CCXCIV'), (312, 'CCCXII'), 
    (421, 'CDXXI'), (528, 'DXXVIII'), (621, 'DCXXI'), (782, 'DCCLXXXII'), (870, 'DCCCLXX'), (941, 'CMXLI'), (1043, 'MXLIII'), 
    (1110, 'MCX'), (1226, 'MCCXXVI'), (1301, 'MCCCI'), (1485, 'MCDLXXXV'), (1509, 'MDIX'), (1607, 'MDCVII'), (1754, 'MDCCLIV'), 
    (1832, 'MDCCCXXXII'), (1993, 'MCMXCIII'), (2074, 'MMLXXIV'), (2152, 'MMCLII'), (2212, 'MMCCXII'), (2343, 'MMCCCXLIII'),
    (2499, 'MMCDXCIX'), (2574, 'MMDLXXIV'), (2646, 'MMDCXLVI'), (2723, 'MMDCCXXIII'),  (2892, 'MMDCCCXCII'), (2975, 'MMCMLXXV'), 
    (3051, 'MMMLI'), (3185, 'MMMCLXXXV'), (3250, 'MMMCCL'), (3313, 'MMMCCCXIII'), (3408, 'MMMCDVIII'), (3501, 'MMMDI'), (3610, 'MMMDCX'), 
    (3743, 'MMMDCCXLIII'), (3844, 'MMMDCCCXLIV'), (3888, 'MMMDCCCLXXXVIII'), (3940, 'MMMCMXL'), (3999, 'MMMCMXCIX'))

    def test_to_roman_known_values(self): 
        # to_roman, known result with known input
        for integer, numeral in self.known_roman:
            result = roman.to_roman(integer) 
            self.assertEqual(numeral, result)

    def test_from_roman_known_values(self):
        # from_roman, known result with known input
        for integer, numeral in self.known_roman:
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)

class ToRomanBadInput(unittest.TestCase): 
    def test_too_large(self): 
        # to_roman, fail with input to large
        self.assertRaises(roman.RangeError, roman.to_roman, 4000)

    def test_zero(self):
        # to_roman, fail with input 0
        self.assertRaises(roman.RangeError, roman.to_roman, 0)

    def test_negative(self):
        # to_roman, fail with input negative
        self.assertRaises(roman.RangeError, roman.to_roman, -1)

    def test_non_integer(self):
        # to_roman, fail with input non-integer
        self.assertRaises(roman.IntError, roman.to_roman, 0.5)

    def test_string(self):
        # to_roman, fail with input string
        self.assertRaises(roman.IntError, roman.to_roman, 't' )

class RoundtripCheck(unittest.TestCase):
    def test_roundtrip(self):
        # from_roman, to_roman(I)
        for integer in range(1, 4000):
            numeral = roman.to_roman(integer)
            result = roman.from_roman(numeral)
            self.assertEqual(integer, result)

class FromRomanBadInput(unittest.TestCase):
    def test_too_many_repeated_numerals(self):
        # from_roman, fail if too many repeated nums
        for R in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(roman.RomanError, roman.from_roman, R)

    def test_repeated_pairs(self):
        # from_roman, fail if repeated pairs of nums
        for R in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(roman.RomanError, roman.from_roman, R)

    def test_malformed_antecedents(self):
        # from_roman, fail with deformed antecedents
        for R in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
            'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(roman.RomanError, roman.from_roman, R)

    def testBlank(self):
        # from_roman, fail with blank str
        self.assertRaises(roman.RomanError, roman.from_roman, '')
    
    def test_non_string(self):
        # from_roman, fail with input non-string
        self.assertRaises(roman.RomanError, roman.from_roman, 1)

if __name__ == '__main__':
    unittest.main()
 