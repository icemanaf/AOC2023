import unittest
from impl import greater_than
from impl import create_rgb
from impl import part_one
from impl import part_two


class TestDay02(unittest.TestCase):
   
    def test_comparisons(self):
        rgb1=(1,2,1)
        rgb2=(1,1,1)
        self.assertTrue(greater_than(rgb1,rgb2))


    def test_create_rgb(self):
        self.assertEqual(create_rgb("1 green, 1 blue"),(0,1,1))
        self.assertEqual(create_rgb(" 6 red, 1 blue, 3 green"),(6,3,1))


    # def test_part_one(self):
    #     sum=part_one()
    #     print(sum)

    def testt_part_two(self):
        sum=part_two()
        print(sum)

if __name__ == '__main__':
    unittest.main()