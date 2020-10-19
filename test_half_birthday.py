"""
Program: test_half_birthday.py
Author: Cara Krug cjkrug@dmacc.edu
Last date modified: 10/19/2020
Purpose: test the datetime functionality of half birthday calculation
"""

import datetime
import unittest
from more_fun_with_collections import half_birthday as hbd


class MyTestCase(unittest.TestCase):
    def test_average(self):
        birthday = datetime.datetime(2020, 6, 22)
        expected_half = datetime.datetime(2020, 12, 21)
        self.assertEqual(expected_half, hbd.half_birthday(birthday))


if __name__ == '__main__':
    unittest.TestCase()
