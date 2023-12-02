import unittest

from impl import get_first_and_last_numbers
from impl import get_first_and_last_number_index
from impl import get_first_and_last_numbers_ex
from impl import part_one,part_two

class TestDay01(unittest.TestCase):

    def test_firstAndLastNumber(self):
        self.assertEqual(get_first_and_last_numbers("1abc2"),12)
        self.assertEqual(get_first_and_last_numbers("a1b2c3d4e5f"),15)
        self.assertEqual(get_first_and_last_numbers("treb7uchet"),77)
      

    def test_get_first_and_last_number_index(self):
        self.assertEqual(get_first_and_last_number_index("1abc2"),(('1',0),('2',4)))
        self.assertEqual(get_first_and_last_number_index("treb7uchet"),(('7',4),('7',4)))


    def test_get_first_and_last_number_ex(self):
        self.assertEqual(get_first_and_last_numbers_ex("two1nine"),29)
        self.assertEqual(get_first_and_last_numbers_ex("eightwothree"),83)
        self.assertEqual(get_first_and_last_numbers_ex("abcone2threexyz"),13)
        self.assertEqual(get_first_and_last_numbers_ex("xtwone3four"),24)
        self.assertEqual(get_first_and_last_numbers_ex("4nineeightseven2"),42)
        self.assertEqual(get_first_and_last_numbers_ex("zoneight234"),14)
        self.assertEqual(get_first_and_last_numbers_ex("7pqrstsixteen"),76)
        self.assertEqual(get_first_and_last_numbers_ex("treb7uchet"),77)
        self.assertEqual(get_first_and_last_numbers_ex("1abc2"),12)
        self.assertEqual(get_first_and_last_numbers_ex("6twotwo18eightthreeeight"),68)


    def test_part_one(self):
       print("part one answwer " + str(part_one()))

    

    def test_part_two(self):
        print("part two answwer " + str(part_two()))

if __name__ == '__main__':
    unittest.main()